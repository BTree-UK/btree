// BTree contact form API (Cloudflare Worker).
//
// POST /contact  ->  checks the form, verifies Cloudflare Turnstile, stores the
// enquiry in D1 and emails it to the team through Microsoft Graph.
// A daily cron deletes enquiries older than the retention period in the privacy notice.

const LIMITS = { name: 100, email: 254, company: 120, phone: 40, service: 80, message: 5000, page: 200 };
// Same rule as the form in assets/js/site.js: a sensible local part, an @, and a real-looking domain with a TLD.
const EMAIL_RE = /^[a-z0-9.!#$%&'*+/=?^_`{|}~-]+@(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,63}$/i;
const RETENTION_MONTHS = 24;

// Throwaway inbox services. Not exhaustive: it stops the common ones.
const DISPOSABLE = new Set([
  'mailinator.com', 'guerrillamail.com', 'guerrillamail.net', 'sharklasers.com', 'grr.la', '10minutemail.com',
  'tempmail.com', 'temp-mail.org', 'tempmailo.com', 'yopmail.com', 'trashmail.com', 'getnada.com', 'dispostable.com',
  'maildrop.cc', 'throwawaymail.com', 'fakeinbox.com', 'mailnesia.com', 'mintemail.com', 'emailondeck.com', 'mohmal.com',
]);

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const cors = corsHeaders(request.headers.get('Origin'), env);

    if (request.method === 'OPTIONS') return new Response(null, { status: 204, headers: cors });

    // Live check used by the form when the visitor leaves the email field.
    if (url.pathname === '/check-email') {
      if (request.method !== 'POST') return json({ error: 'Method not allowed.' }, 405, cors);
      if (!cors['Access-Control-Allow-Origin']) return json({ error: 'Origin not allowed.' }, 403);
      let body = {};
      try { body = await request.json(); } catch {}
      const error = await emailProblem(clean(body.email, LIMITS.email).toLowerCase());
      return json(error ? { ok: false, error } : { ok: true }, 200, cors);
    }

    if (url.pathname !== '/contact') return json({ error: 'Not found.' }, 404, cors);
    if (request.method !== 'POST') return json({ error: 'Method not allowed.' }, 405, cors);
    if (!cors['Access-Control-Allow-Origin']) return json({ error: 'Origin not allowed.' }, 403);

    let data;
    try {
      data = await request.json();
    } catch {
      return json({ error: 'Invalid request.' }, 400, cors);
    }

    // Honeypot: real visitors never see or fill the "website" field. Pretend it worked.
    if (data.website) return json({ ok: true }, 200, cors);

    const f = {};
    for (const [key, max] of Object.entries(LIMITS)) f[key] = clean(data[key], max);
    f.email = f.email.toLowerCase();

    const missing = ['name', 'email', 'message'].filter((k) => !f[k]);
    if (missing.length) return json({ error: 'Please fill in your name, email and message.' }, 400, cors);
    const emailError = await emailProblem(f.email);
    if (emailError) return json({ error: emailError, field: 'email' }, 400, cors);

    const ip = request.headers.get('CF-Connecting-IP') || '';
    if (!(await verifyTurnstile(env, data.turnstileToken, ip))) {
      return json({ error: 'The spam check failed. Please try again.' }, 400, cors);
    }

    const rec = {
      id: crypto.randomUUID(),
      created_at: new Date().toISOString(),
      ...f,
      country: (request.cf && request.cf.country) || '',
    };

    await env.DB.prepare(
      `INSERT INTO enquiries (id, created_at, name, email, company, phone, service, message, page, country)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`
    )
      .bind(rec.id, rec.created_at, rec.name, rec.email, rec.company, rec.phone, rec.service, rec.message, rec.page, rec.country)
      .run();

    // Email after responding; the enquiry is already safe in D1 if this fails.
    ctx.waitUntil(
      notify(env, rec)
        .then((sent) => sent && env.DB.prepare('UPDATE enquiries SET notified = 1 WHERE id = ?').bind(rec.id).run())
        .catch((err) => console.error('notify failed', rec.id, err))
    );

    return json({ ok: true }, 200, cors);
  },

  async scheduled(event, env) {
    const cutoff = new Date();
    cutoff.setUTCMonth(cutoff.getUTCMonth() - RETENTION_MONTHS);
    await env.DB.prepare('DELETE FROM enquiries WHERE created_at < ?').bind(cutoff.toISOString()).run();
  },
};

function corsHeaders(origin, env) {
  const allowed = (env.ALLOWED_ORIGINS || '').split(',').map((s) => s.trim()).filter(Boolean);
  const h = { 'Access-Control-Allow-Methods': 'POST, OPTIONS', 'Access-Control-Allow-Headers': 'Content-Type', 'Access-Control-Max-Age': '86400', Vary: 'Origin' };
  if (origin && allowed.includes(origin)) h['Access-Control-Allow-Origin'] = origin;
  return h;
}

function json(body, status, headers = {}) {
  return new Response(JSON.stringify(body), { status, headers: { 'Content-Type': 'application/json', ...headers } });
}

function clean(value, max) {
  return String(value ?? '').replace(/\u0000/g, '').trim().slice(0, max);
}

// Returns a message for the visitor if the address cannot be right, or '' if it looks deliverable.
async function emailProblem(email) {
  if (!email) return 'Please enter your email address.';
  const [local, domain] = email.split('@');
  if (email.length > 254 || !EMAIL_RE.test(email) || local.length > 64 || /\.\./.test(email) || local.startsWith('.') || local.endsWith('.')) {
    return 'Please enter a valid email address, like name@company.co.uk.';
  }
  if (DISPOSABLE.has(domain)) return 'Please use your work or personal email address, not a temporary one.';

  // Can the domain receive email? MX records, or an A record as the fallback mail host.
  const mx = await dnsLookup(domain, 'MX');
  if (mx === null) return ''; // DNS lookup failed: give the visitor the benefit of the doubt
  if (mx.length) {
    const nullMx = mx.every((r) => /^0\s+\.?$/.test(r.trim())); // RFC 7505 "this domain accepts no mail"
    return nullMx ? 'That email domain does not accept email. Please check the address.' : '';
  }
  const a = await dnsLookup(domain, 'A');
  if (a === null || a.length) return '';
  return `We could not find "${domain}". Please check for typos.`;
}

// DNS over HTTPS through Cloudflare. Returns the record data, [] when there are none, or null on failure.
async function dnsLookup(name, type) {
  try {
    const res = await fetch(`https://cloudflare-dns.com/dns-query?name=${encodeURIComponent(name)}&type=${type}`, {
      headers: { accept: 'application/dns-json' },
    });
    if (!res.ok) return null;
    const out = await res.json();
    if (out.Status === 3) return []; // NXDOMAIN: the domain does not exist
    if (out.Status !== 0) return null;
    const code = type === 'MX' ? 15 : 1;
    return (out.Answer || []).filter((r) => r.type === code).map((r) => String(r.data));
  } catch {
    return null;
  }
}

async function verifyTurnstile(env, token, ip) {
  if (!token || !env.TURNSTILE_SECRET) return false;
  const body = new FormData();
  body.append('secret', env.TURNSTILE_SECRET);
  body.append('response', String(token));
  if (ip) body.append('remoteip', ip);
  const res = await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify', { method: 'POST', body });
  const out = await res.json();
  return out.success === true;
}

// Sends the enquiry to MAIL_TO from the MAIL_FROM mailbox using Microsoft Graph
// (app-only, Mail.Send). Returns false when Graph is not configured.
async function notify(env, rec) {
  if (!env.MS_TENANT_ID || !env.MS_CLIENT_ID || !env.MS_CLIENT_SECRET || !env.MAIL_FROM || !env.MAIL_TO) return false;

  const tokenRes = await fetch(`https://login.microsoftonline.com/${env.MS_TENANT_ID}/oauth2/v2.0/token`, {
    method: 'POST',
    body: new URLSearchParams({
      client_id: env.MS_CLIENT_ID,
      client_secret: env.MS_CLIENT_SECRET,
      scope: 'https://graph.microsoft.com/.default',
      grant_type: 'client_credentials',
    }),
  });
  if (!tokenRes.ok) throw new Error(`token ${tokenRes.status}: ${await tokenRes.text()}`);
  const { access_token } = await tokenRes.json();

  const oneLine = (s) => s.replace(/[\r\n]+/g, ' ');
  const lines = [
    `Name:    ${rec.name}`,
    `Email:   ${rec.email}`,
    `Company: ${rec.company || '-'}`,
    `Phone:   ${rec.phone || '-'}`,
    `Service: ${rec.service || '-'}`,
    `Page:    ${rec.page || '-'}`,
    `Country: ${rec.country || '-'}`,
    `Time:    ${rec.created_at}`,
    `ID:      ${rec.id}`,
    '',
    rec.message,
  ];

  const mailRes = await fetch(`https://graph.microsoft.com/v1.0/users/${encodeURIComponent(env.MAIL_FROM)}/sendMail`, {
    method: 'POST',
    headers: { Authorization: `Bearer ${access_token}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      message: {
        subject: oneLine(`New enquiry: ${rec.service || 'General'} from ${rec.name}${rec.company ? ` (${rec.company})` : ''}`),
        body: { contentType: 'Text', content: lines.join('\n') },
        toRecipients: env.MAIL_TO.split(',').map((a) => ({ emailAddress: { address: a.trim() } })),
        replyTo: [{ emailAddress: { address: rec.email, name: oneLine(rec.name) } }],
      },
      saveToSentItems: false,
    }),
  });
  if (!mailRes.ok) throw new Error(`sendMail ${mailRes.status}: ${await mailRes.text()}`);
  return true;
}
