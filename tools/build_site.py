"""Generate the BTree company pages (home + service pages) as static HTML."""
import pathlib, re, sys

ROOT = pathlib.Path(sys.argv[1])
SITE = "https://btree.uk/"

# Registered company details (Companies House), shown in the footer and the privacy notice.
COMPANY = {
    "name": "BTree Technologies Limited",
    "number": "16621870",
    "location": "Bradford, United Kingdom",
}
COMPANY_LINE = (f'{COMPANY["name"]}. Registered in England and Wales, company number {COMPANY["number"]}. '
                f'{COMPANY["location"]}.')

# Cache-busting: pages load site.css?v=<hash> and site.js?v=<hash>, so browsers fetch
# the new file as soon as its contents change instead of using a stale cached copy.
import hashlib
def _ver(path):
    return hashlib.sha1((ROOT / path).read_bytes()).hexdigest()[:8]
CSS_V, JS_V = _ver("assets/css/site.css"), _ver("assets/js/site.js")

sf = (ROOT / "shiftflow/index.html").read_text(encoding="utf-8")
def sym(i):
    m = re.search(r'  <symbol id="%s".*?</symbol>' % re.escape(i), sf)
    return m.group(0)

NEW_SYMBOLS = {
    "i-code": '<path d="m16 18 6-6-6-6M8 6l-6 6 6 6"/>',
    "i-network": '<rect x="16" y="16" width="6" height="6" rx="1"/><rect x="2" y="16" width="6" height="6" rx="1"/><rect x="9" y="2" width="6" height="6" rx="1"/><path d="M5 16v-3a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v3M12 12V8"/>',
    "i-cloud": '<path d="M17.5 19H9a7 7 0 1 1 6.71-9h1.79a4.5 4.5 0 1 1 0 9z"/>',
    "i-grid": '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/>',
    "i-spark": '<path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9z"/><path d="M19 15l.8 2.2L22 18l-2.2.8L19 21l-.8-2.2L16 18l2.2-.8z"/>',
    "i-check": '<path d="M20 6 9 17l-5-5"/>',
    "i-pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
}
SPRITE = "\n".join(
    [sym(i) for i in ["i-shield", "i-lock", "i-layers", "i-gear", "i-users", "i-calendar", "i-arrow", "i-mail", "i-menu", "i-chev", "i-send"]]
    + ['  <symbol id="%s" viewBox="0 0 24 24">%s</symbol>' % (k, v) for k, v in NEW_SYMBOLS.items()]
)

SERVICES = [
    {
        "slug": "software-development", "icon": "i-code", "name": "Software development",
        "short": "Web and mobile apps, integrations and modernisation, built around how your business works.",
        "title": "Software development | BTree",
        "desc": "Custom web and mobile applications, system integrations and legacy modernisation from BTree, a UK software and technology company.",
        "h1": 'Software built around <span class="grad">how you work.</span>',
        "sub": "From a single integration to a complete product, we design, build and support software that fits your processes instead of forcing you to change them. We built ShiftFlow ourselves, so we know what it takes to take software from idea to everyday use.",
        "offer": [
            ("Web applications", "Secure, fast business applications and portals that work in any browser."),
            ("Mobile apps", "iOS and Android apps for your staff or your customers."),
            ("Integrations and APIs", "Connect the systems you already use, such as accounting, HR, point of sale and CRM, so data flows without re-typing."),
            ("Modernisation", "Move ageing spreadsheets, Access databases and legacy systems onto modern, supported platforms."),
            ("Cloud-native architecture", "Applications designed to scale on Azure or AWS, with security built in from the start."),
            ("DevOps and support", "Automated pipelines, infrastructure as code and ongoing maintenance once you are live."),
        ],
    },
    {
        "slug": "ai-adoption", "icon": "i-spark", "name": "AI adoption",
        "short": "Find where AI really helps, roll out tools like Copilot securely, automate busywork and train your team.",
        "title": "AI adoption | BTree",
        "desc": "Practical AI adoption for UK businesses: AI readiness assessments, Microsoft 365 Copilot roll-out, AI assistants on your own data, workflow automation, AI policy and staff training.",
        "h1": 'Put AI to work, <span class="grad">safely and sensibly.</span>',
        "sub": "AI can save your team hours every week, or leak your data and waste money on tools nobody uses. We help you find where AI genuinely helps, roll it out securely and get your people using it well.",
        "offer": [
            ("AI readiness assessment", "We look at your processes, data and systems, and show where AI will save time or money and where it will not."),
            ("Microsoft 365 Copilot", "Get your data and permissions ready, roll Copilot out to the right people and measure whether it is paying off."),
            ("AI assistants on your data", "Assistants that answer questions from your own documents, policies and systems, for staff or for customers."),
            ("Workflow automation", "Automate repetitive work such as data entry, email triage and reporting with Power Automate, AI agents and integrations."),
            ("AI policy and governance", "Clear rules on which AI tools staff can use and what data they can share, in line with UK GDPR."),
            ("Training and adoption", "Hands-on sessions that show your team how to use AI tools well in their day-to-day work."),
        ],
    },
    {
        "slug": "networks", "icon": "i-network", "name": "Networks, internet and firewalls",
        "short": "Business internet, Wi-Fi, firewalls and multi-site networks that stay up and stay secure.",
        "title": "Networks, internet and firewalls | BTree",
        "desc": "Business internet, Wi-Fi, firewall and multi-site network design, installation and support for UK businesses from BTree.",
        "h1": 'Networks that stay up <span class="grad">and stay secure.</span>',
        "sub": "Your tills, phones, cameras and cloud apps all depend on the network. We design, install and look after connectivity for offices, venues and multi-site businesses, so it is fast, reliable and protected.",
        "offer": [
            ("Business internet", "Help choosing the right fibre or leased line for each site, with 4G or 5G backup so you stay online."),
            ("Firewalls", "Firewall design, set-up and ongoing management, with rules that protect you without getting in the way."),
            ("Wi-Fi", "Coverage planning, staff and guest networks kept separate, and access points that are managed centrally."),
            ("Multi-site and VPN", "Connect sites, remote workers and cloud services securely, with consistent settings everywhere."),
            ("Monitoring and support", "We watch the network, spot problems early and fix them, often before anyone notices."),
            ("Hardware", "Switches, routers and access points specified, configured and documented for your sites."),
        ],
    },
    {
        "slug": "cyber-security", "icon": "i-shield", "name": "Cyber security",
        "short": "Security reviews, Cyber Essentials readiness, MFA, device protection and backup.",
        "title": "Cyber security | BTree",
        "desc": "Practical cyber security for UK businesses: security reviews, Cyber Essentials readiness, MFA and SSO, device and email protection, and backup.",
        "h1": 'Practical security <span class="grad">for real businesses.</span>',
        "sub": "Most attacks start with a weak password, an unpatched device or a convincing email. We find the gaps that matter most in your business and close them, in plain English and in a sensible order.",
        "offer": [
            ("Security reviews", "A clear picture of where you are exposed today, with a prioritised plan to fix it."),
            ("Cyber Essentials readiness", "We help you prepare for Cyber Essentials and Cyber Essentials Plus, and put the controls in place."),
            ("Identity and access", "Multi-factor authentication, single sign-on and access rules so only the right people get in."),
            ("Device and email protection", "Endpoint protection, patching and filtering that stops phishing and malware reaching staff."),
            ("Backup and recovery", "Tested backups for your data and cloud services, so a mistake or an attack is not a disaster."),
            ("Policies and awareness", "Simple policies and staff guidance that make secure habits the easy option."),
        ],
    },
    {
        "slug": "microsoft-365-azure", "icon": "i-grid", "name": "Microsoft 365 and Azure",
        "short": "Microsoft 365 set-up and migration, Teams, SharePoint, Entra ID, Intune and Azure.",
        "title": "Microsoft 365 and Azure | BTree",
        "desc": "Microsoft 365 migration and set-up, Teams and SharePoint, Entra ID, Intune device management and Azure infrastructure from BTree.",
        "h1": 'Get more from <span class="grad">Microsoft 365 and Azure.</span>',
        "sub": "Whether you are moving email for the first time or running a hybrid estate, we set up Microsoft 365 and Azure properly: secure by default, well organised and easy for your team to use.",
        "offer": [
            ("Microsoft 365 set-up and migration", "Move email, files and calendars from Google Workspace, another provider or on-premises Exchange with minimal disruption."),
            ("Teams and SharePoint", "A tidy structure for files, sites and channels, so people can find what they need and share it safely."),
            ("Entra ID", "Identity, single sign-on, MFA and conditional access for Microsoft 365 and your other apps."),
            ("Intune device management", "Laptops and phones set up, secured and updated automatically, wherever your staff work."),
            ("Azure infrastructure", "Move servers and applications to Azure, or build new workloads there, with cost and security under control."),
            ("Exchange and Active Directory", "Support for on-premises and hybrid Exchange and Active Directory, including clean-ups and migrations."),
        ],
    },
    {
        "slug": "aws", "icon": "i-cloud", "name": "AWS cloud",
        "short": "Migration, architecture, infrastructure as code, cost optimisation and security on AWS.",
        "title": "AWS cloud services | BTree",
        "desc": "AWS migration, architecture, infrastructure as code, cost optimisation and security from BTree, a UK cloud and technology company.",
        "h1": 'Build and run on AWS <span class="grad">with confidence.</span>',
        "sub": "AWS gives you enormous flexibility, and plenty of ways to overspend or leave something exposed. We help you design, move and run workloads on AWS so they are secure, resilient and sensibly priced.",
        "offer": [
            ("Migration to AWS", "Plan and move servers, databases and applications to AWS with a clear cut-over and rollback plan."),
            ("Architecture reviews", "Reviews against AWS best practice for security, reliability, performance and cost."),
            ("Infrastructure as code", "Environments defined in Terraform or CloudFormation, so they are repeatable, reviewable and documented."),
            ("Cost optimisation", "Right-sizing, savings plans and clean-ups that bring your monthly bill down."),
            ("Security and governance", "IAM, account structure, logging and guardrails so teams can move fast without creating risk."),
            ("Monitoring and support", "Alerting, backups and ongoing support for the workloads you run on AWS."),
        ],
    },
]

INDUSTRIES = [
    ("Hospitality", "Restaurants, bars, cafes and hotels, where systems have to work on the busiest night of the week."),
    ("Retail", "Shops and multi-site chains that need reliable tills, networks and stock systems at every branch."),
    ("Health and social care", "Care providers handling sensitive data, round-the-clock teams and strict compliance."),
    ("Professional services", "Firms that rely on Microsoft 365, secure remote working and well-protected client data."),
    ("Warehousing and logistics", "Operations that depend on connected sites, devices on the floor and accurate data."),
    ("Manufacturing", "Production sites where downtime is expensive and older systems need to talk to newer ones."),
]

# Partners: (name, logo file, width, height, card style, website or "").
PARTNERS = [
    ("MyLahore", "mylahore.jpg", 640, 240, "light", "https://www.mylahore.co.uk/"),
    ("Wunder Crumble", "wunder-crumble.png", 200, 48, "dark", "https://www.wundercrumble.co.uk/"),
    ("Janan", "janan.png", 152, 45, "dark", ""),
]


def partners_html(r):
    """The partners section: logos glide past in an endless loop (static for reduced motion)."""
    def card(name, img, w, h, style, url, copy):
        logo = f'<img src="{r}assets/partners/{img}" alt="{"" if copy else name}" width="{w}" height="{h}" loading="lazy" />'
        if url:
            tab = ' tabindex="-1"' if copy else ""
            logo = f'<a href="{url}" target="_blank" rel="noopener"{tab}>{logo}</a>'
        hidden = ' aria-hidden="true"' if copy else ""
        return f'<li class="partner partner--{style}"{hidden}>{logo}</li>'
    # One set only, so crawlers see each partner link once; site.js adds the copies the loop needs.
    cards = [card(*pt, copy=False) for pt in PARTNERS]
    track = "\n          ".join(cards)
    return f'''<section class="partners" id="partners" aria-labelledby="partnersTitle">
    <div class="wrap partners__head reveal">
      <span class="eyebrow">Our partners</span>
      <h2 id="partnersTitle">In <span class="grad">good company</span></h2>
      <p class="lead">Businesses we are proud to build, run and grow with.</p>
    </div>
    <div class="marquee">
      <ul class="marquee__track">
          {track}
      </ul>
    </div>
  </section>'''


# ShiftFlow used to live at /. Send its old deep links (btree.uk/#kiosk etc.) to /shiftflow/.
REDIRECT = """  <script>(function () { var h = location.hash.slice(1); if (/^(features|all-features|apps|mobile|kiosk|views|compliance|security)$/.test(h)) location.replace('shiftflow/#' + h); })();</script>
"""

import json as _json
from html import escape as _esc

ORG_ID = SITE + "#org"
ORG = {
    "@type": "Organization", "@id": ORG_ID, "name": "BTree", "legalName": COMPANY["name"], "url": SITE,
    "logo": SITE + "assets/icons/apple-touch-icon.png", "email": "info@btree.uk",
    "address": {"@type": "PostalAddress", "addressLocality": "Bradford", "addressCountry": "GB"}, "areaServed": "GB",
    "description": "UK technology company offering software development, AI adoption, networks, cyber security, "
                   "Microsoft 365, Azure and AWS, and the ShiftFlow workforce platform.",
}


def breadcrumbs(*items):
    """BreadcrumbList from (name, url) pairs, starting at the home page."""
    trail = [("Home", SITE)] + list(items)
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(trail)]}


def seo_tags(r, title, desc, url, image="btree.png", image_alt="BTree", ld=(), icon="btree"):
    """Canonical, Open Graph, Twitter card, icons and JSON-LD for one page."""
    t, d = _esc(title), _esc(desc)
    img = f"{SITE}assets/og/{image}"
    icons = {"btree": ("btree-icon.svg", "favicon-48.png", "apple-touch-icon.png"),
             "shiftflow": ("favicon.svg", "shiftflow-48.png", "shiftflow-touch-icon.png")}[icon]
    graph = _json.dumps({"@context": "https://schema.org", "@graph": [ORG, *ld]}, ensure_ascii=False)
    return f'''  <link rel="canonical" href="{url}" />
  <meta property="og:site_name" content="BTree" />
  <meta property="og:locale" content="en_GB" />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="{t}" />
  <meta property="og:description" content="{d}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="{img}" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:image:alt" content="{_esc(image_alt)}" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{t}" />
  <meta name="twitter:description" content="{d}" />
  <meta name="twitter:image" content="{img}" />
  <link rel="icon" href="{r}assets/{icons[0]}" type="image/svg+xml" />
  <link rel="icon" href="{r}assets/icons/{icons[1]}" type="image/png" sizes="48x48" />
  <link rel="apple-touch-icon" href="{r}assets/icons/{icons[2]}" />
  <script type="application/ld+json">{graph}</script>
'''

def robots_noindex(r):
    """Error pages: keep them out of search results and do not pretend to be another URL."""
    return f'''  <meta name="robots" content="noindex" />
  <link rel="icon" href="{r}assets/btree-icon.svg" type="image/svg+xml" />
  <link rel="icon" href="{r}assets/icons/favicon-48.png" type="image/png" sizes="48x48" />
'''


def head(r, title, desc, url, ld=(), noindex=False):
    return f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{_esc(desc)}" />
  <meta name="theme-color" content="#070f2b" />
{robots_noindex(r) if noindex else seo_tags(r, title, desc, url, ld=ld)}  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{r}assets/css/site.css?v={CSS_V}" />
  <style>svg.i {{ fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }}</style>
{REDIRECT if r == "" else ""}</head>
<body>

<svg width="0" height="0" style="position:absolute" aria-hidden="true">
{SPRITE}
</svg>
'''


def nav(r):
    svc = "\n".join(f'          <li><a href="{r}services/{s["slug"]}/">{s["name"]}</a></li>' for s in SERVICES)
    return f'''
<header class="nav" id="nav">
  <div class="wrap nav__inner">
    <a class="brand brand--btree" href="{r or './'}" aria-label="BTree home">{{btree}}</a>
    <ul class="nav__links" id="navLinks">
      <li class="has-menu"><a href="{r}#services">Services</a>
        <ul class="submenu">
{svc}
        </ul>
      </li>
      <li class="has-menu"><a href="{r}#products">Products</a>
        <ul class="submenu">
          <li><a href="{r}shiftflow/">ShiftFlow <em class="soon soon--live">Live</em></a></li>
          <li><span>CRM <em class="soon">Coming soon</em></span></li>
          <li><span>EventFlow <em class="soon">Coming soon</em></span></li>
        </ul>
      </li>
      <li><a href="{r}#industries">Industries</a></li>
      <li><a href="{r}#about">About</a></li>
    </ul>
    <a class="btn btn--primary nav__cta" href="#contact">Get in touch</a>
    <button class="nav__toggle" id="navToggle" aria-label="Open menu" aria-expanded="false" aria-controls="navLinks">
      <svg class="i"><use href="#i-menu"/></svg>
    </button>
  </div>
</header>
'''


# Contact form backend: the Cloudflare Worker in /worker.
CONTACT_API = "https://forms.btree.uk/contact"
# Cloudflare Turnstile site key (public). For a quick local test without Cloudflare,
# Cloudflare's always-pass test key is "1x00000000000000000000AA".
TURNSTILE_SITE_KEY = "0x4AAAAAAGKb1RyDSb_FAl75"


def contact_form(r, service="", button="Send message"):
    """The enquiry form, shared by every page (ShiftFlow included)."""
    choices = [(x["name"], x["icon"]) for x in SERVICES] + [("ShiftFlow", "i-calendar"), ("Something else", "i-mail")]
    opts = "\n".join(
        f'              <option data-icon="{ic}"{" selected" if n == service else ""}>{n}</option>' for n, ic in choices)
    # Pages outside this generator (ShiftFlow) may lack the service icons, so carry them along.
    sprite = ""
    if r == "../":
        missing = [x["icon"] for x in SERVICES if f'<symbol id="{x["icon"]}"' not in sf]
        sprite = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true">'
                  + "".join(f'<symbol id="{k}" viewBox="0 0 24 24">{NEW_SYMBOLS[k]}</symbol>' for k in missing if k in NEW_SYMBOLS)
                  + "</svg>\n          ")
    return f'''<form class="form" action="{CONTACT_API}" method="post" data-contact>
          <div class="form__row">
            <label>Name<input name="name" autocomplete="name" required maxlength="100" /></label>
            <label>Email<input type="email" name="email" autocomplete="email" required maxlength="254" /></label>
          </div>
          <div class="form__row">
            <label>Company <span>(optional)</span><input name="company" autocomplete="organization" maxlength="120" /></label>
            <label>Phone <span>(optional)</span><input type="tel" name="phone" autocomplete="tel" maxlength="40" /></label>
          </div>
          {sprite}<div class="field">
            <span class="field__label" id="service-label">What do you need help with?</span>
            <select name="service" required aria-labelledby="service-label" data-enhance>
              <option value=""{"" if service else " selected"} disabled>Choose one</option>
{opts}
            </select>
          </div>
          <label>Message<textarea name="message" rows="4" required maxlength="5000"></textarea></label>
          <div class="form__hp" aria-hidden="true"><label>Leave this empty<input name="website" tabindex="-1" autocomplete="off" /></label></div>
          <div class="turnstile" data-sitekey="{TURNSTILE_SITE_KEY}"></div>
          <button class="btn btn--primary" type="submit"><svg class="i"><use href="#i-send"/></svg> {button}</button>
          <p class="form__status" role="status" aria-live="polite"></p>
          <p class="form__note">We only use your details to reply to you. See our <a href="{r}privacy/">privacy notice</a>, or email <a href="mailto:info@btree.uk">info@btree.uk</a>.</p>
        </form>
        <script src="https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit" async defer></script>'''


def contact(r, heading, lead, service=""):
    return f'''
  <!-- Contact -->
  <section class="section" id="contact">
    <div class="wrap">
      <div class="cta cta--form reveal">
        <div>
          <span class="eyebrow">Get in touch</span>
          <h2>{heading}</h2>
          <p class="lead">{lead}</p>
        </div>
        {contact_form(r, service)}
      </div>
    </div>
  </section>
'''


def footer(r):
    svc = "\n".join(f'        <li><a href="{r}services/{s["slug"]}/">{s["name"]}</a></li>' for s in SERVICES)
    return f'''
</main>

<footer class="footer footer--btree">
  <div class="wrap">
    <div class="footer__cols">
      <div>
        <a class="brand brand--btree" href="{r or './'}">{{btree}}</a>
        <p>A UK technology company. We build software, help businesses adopt AI, run secure networks and cloud platforms, and make products for growing businesses.</p>
      </div>
      <nav aria-label="Services"><h4>Services</h4><ul>
{svc}
      </ul></nav>
      <nav aria-label="Products"><h4>Products</h4><ul>
        <li><a href="{r}shiftflow/">ShiftFlow</a></li>
        <li><a href="https://shiftflow.btree.uk">ShiftFlow sign in</a></li>
        <li><span>CRM (coming soon)</span></li>
        <li><span>EventFlow (coming soon)</span></li>
      </ul></nav>
      <nav aria-label="Company"><h4>Company</h4><ul>
        <li><a href="{r}#about">About</a></li>
        <li><a href="{r}#industries">Industries</a></li>
        <li><a href="{r}#partners">Partners</a></li>
        <li><a href="{r}#contact">Contact us</a></li>
        <li><a href="{r}privacy/">Privacy notice</a></li>
      </ul></nav>
    </div>
    <div class="footer__base">
      <span>&copy; <span id="year">2026</span> {{btree}}. All rights reserved.</span>
      <span class="footer__legal">{COMPANY_LINE}</span>
    </div>
  </div>
</footer>

<script src="{r}assets/js/site.js?v={JS_V}" defer></script>
</body>
</html>
'''


def svc_card(r, s, compact=False):
    cls = "svc svc--compact" if compact else "svc"
    return f'''        <a class="{cls} reveal" href="{r}services/{s["slug"]}/">
          <span class="svc__ico"><svg class="i"><use href="#{s["icon"]}"/></svg></span>
          <h3>{s["name"]}</h3>
          <p>{s["short"]}</p>
          <span class="svc__more">Learn more <svg class="i"><use href="#i-arrow"/></svg></span>
        </a>'''


# ---------- Home ----------
def term_lines(lines, start=0):
    return "".join(f'<span class="ln" style="--d:{i + start}">{line or "&nbsp;"}</span>' for i, line in enumerate(lines))

OK = '<span class="t-dim">[</span><span class="t-ok">&nbsp;OK&nbsp;</span><span class="t-dim">]</span>'
HERO_TERM = term_lines([
    '<span class="t-p">$</span> btree status --your-business',
    f'{OK} network       <span class="t-dim">fast and secure</span>',
    f'{OK} firewall      <span class="t-dim">holding the line</span>',
    f'{OK} microsoft365  <span class="t-dim">set up properly</span>',
    f'{OK} cloud         <span class="t-dim">scaling on demand</span>',
    f'{OK} ai            <span class="t-dim">put to work</span>',
    f'{OK} shiftflow     <span class="t-dim">rota published</span>',
    '',
    '<span class="t-ok">&gt; all systems go</span>',
    '<span class="t-p">$</span> <span class="term__cursor"></span>',
], start=2)

r = ""
home = head(r, "BTree | Software, AI, networks, cyber security and cloud for UK businesses",
            "BTree is a UK technology company offering software development, AI adoption, networks and firewalls, cyber security, Microsoft 365, Azure and AWS, and products like ShiftFlow.",
            SITE, ld=[{"@type": "WebSite", "@id": SITE + "#website", "url": SITE, "name": "BTree", "publisher": {"@id": ORG_ID}}])
home += nav(r)
home += f'''
<main id="top">

  <!-- Hero -->
  <section class="hero hero--company">
    <span class="hero__glow" aria-hidden="true"></span>
    <div class="wrap hero__split">
      <div class="hero__copy hero__copy--left">
        <h1>Technology that keeps your business <span class="rot" data-words="moving.|secure.|online.|growing.|ahead."><span class="grad rot__word" data-text="moving.">moving.</span></span></h1>
        <p class="hero__sub">BTree is a UK technology company. We build software, help businesses adopt AI, run secure networks and cloud platforms, and make products like ShiftFlow for businesses that want their technology to just work.</p>
        <div class="hero__actions">
          <a class="btn btn--primary" href="#contact">Talk to us <svg class="i"><use href="#i-arrow"/></svg></a>
          <a class="btn btn--ghost" href="#services">Explore our services</a>
        </div>
      </div>
      <div class="term term--hero" role="img" aria-label="A terminal showing BTree checking a business: network, firewall, Microsoft 365, cloud, AI and ShiftFlow are all OK.">
        <div class="term__bar" aria-hidden="true"><i></i><i></i><i></i><span>btree@ops: ~</span></div>
        <pre class="term__out" aria-hidden="true"><code>{HERO_TERM}</code></pre>
      </div>
    </div>
  </section>

  <!-- Trust strip -->
  <section class="strip strip--tight" aria-label="Why BTree">
    <div class="wrap">
      <ul>
        <li><svg class="i"><use href="#i-pin"/></svg><div><b>UK based</b>Designed, built and supported in the UK.</div></li>
        <li><svg class="i"><use href="#i-layers"/></svg><div><b>One partner</b>Software, AI, networks, security and cloud under one roof.</div></li>
        <li><svg class="i"><use href="#i-lock"/></svg><div><b>Security first</b>Every project starts with protecting your data.</div></li>
        <li><svg class="i"><use href="#i-gear"/></svg><div><b>Build and run</b>We stay on to support what we deliver.</div></li>
      </ul>
    </div>
  </section>

  <!-- Services -->
  <section class="section" id="services">
    <div class="wrap">
      <div class="section-head center reveal">
        <span class="eyebrow">Services</span>
        <h2>Everything your technology needs</h2>
        <p class="lead">From the network in your building to the software your team uses every day, we design it, build it and look after it.</p>
      </div>
      <div class="svc-grid">
{chr(10).join(svc_card(r, s) for s in SERVICES)}
      </div>
    </div>
  </section>

  <!-- Products -->
  <section class="section section--soft" id="products">
    <div class="wrap">
      <div class="section-head center reveal">
        <span class="eyebrow">Products</span>
        <h2>Software we build and run ourselves</h2>
        <p class="lead">Our products come from problems we have solved for real businesses, turned into software anyone can use.</p>
      </div>
      <div class="products">
        <a class="product product--live reveal" href="shiftflow/">
          <div class="product__top"><img src="assets/favicon.svg" alt="" width="44" height="44" /><span class="soon soon--live">Available now</span></div>
          <h3>ShiftFlow</h3>
          <p>Rotas, kiosk clock-in, timesheets, HR and UK compliance for shift-based teams, with an employee app for iOS and Android.</p>
          <span class="svc__more">Explore ShiftFlow <svg class="i"><use href="#i-arrow"/></svg></span>
        </a>
        <div class="product reveal">
          <div class="product__top"><span class="product__ico"><svg class="i"><use href="#i-users"/></svg></span><span class="soon">Coming soon</span></div>
          <h3>CRM</h3>
          <p>Customers, leads and follow-ups in one place, built for small and growing teams.</p>
        </div>
        <div class="product reveal">
          <div class="product__top"><span class="product__ico"><svg class="i"><use href="#i-calendar"/></svg></span><span class="soon">Coming soon</span></div>
          <h3>EventFlow</h3>
          <p>Plan and run events from first enquiry to the team on the day.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Industries -->
  <section class="section" id="industries">
    <div class="wrap">
      <div class="section-head center reveal">
        <span class="eyebrow">Industries</span>
        <h2>Who we work with</h2>
        <p class="lead">We work with businesses of every size. These are the sectors we know best.</p>
      </div>
      <div class="industries">
{chr(10).join(f'        <div class="ind reveal"><h3>{t}</h3><p>{d}</p></div>' for t, d in INDUSTRIES)}
      </div>
    </div>
  </section>

  <!-- Partners -->
  {partners_html(r)}

  <!-- About -->
  <section class="section" id="about">
    <div class="wrap btree">
      <div class="reveal">
        <span class="eyebrow">Who we are</span>
        <div class="btree__logo">{{btree}}</div>
      </div>
      <div class="reveal">
        <p class="lead" style="color:var(--text)">{{btree}} is a technology company that blends deep technical expertise with business insight to build scalable, smart and sustainable digital products. We work as an extension of your team, from the first conversation to long-term support.</p>
        <ul class="services">
          <li><b>Plain-English advice</b>Clear recommendations and honest pricing, without the jargon.</li>
          <li><b>Hands-on delivery</b>The people who design your solution are the people who build it.</li>
          <li><b>Long-term support</b>We look after what we deliver, and keep improving it.</li>
          <li><b>Products as well as services</b>We run our own software, so we understand yours.</li>
        </ul>
      </div>
    </div>
  </section>
'''
home += contact(r, "Let's talk about your technology",
                "Whether you need a new system built, a network sorted or a second opinion on security, we are happy to help.")
home += footer(r)
(ROOT / "index.html").write_text(home, encoding="utf-8")

# ---------- Service pages ----------
STEPS = [
    ("Understand", "We start by listening: how your business works, what is slowing you down and what good looks like."),
    ("Plan", "A clear proposal with options, costs and timings, so you know exactly what you are getting."),
    ("Deliver", "We do the work with minimal disruption, keeping you updated at every step."),
    ("Support", "We stay on to look after it, fix issues quickly and keep things improving."),
]
for s in SERVICES:
    r = "../../"
    url = f"{SITE}services/{s['slug']}/"
    page = head(r, s["title"], s["desc"], url, ld=[
        {"@type": "Service", "name": s["name"], "serviceType": s["name"], "description": s["desc"], "url": url,
         "provider": {"@id": ORG_ID}, "areaServed": {"@type": "Country", "name": "United Kingdom"}},
        breadcrumbs(("Services", SITE + "#services"), (s["name"], url))]) + nav(r)
    others = [o for o in SERVICES if o is not s]
    page += f'''
<main id="top">

  <section class="hero hero--page">
    <div class="wrap">
      <div class="hero__copy">
        <nav class="crumbs" aria-label="Breadcrumb"><a href="{r}">Home</a> <span>/</span> <a href="{r}#services">Services</a> <span>/</span> {s["name"]}</nav>
        <span class="eyebrow">{s["name"]}</span>
        <h1>{s["h1"]}</h1>
        <p class="hero__sub">{s["sub"]}</p>
        <div class="hero__actions">
          <a class="btn btn--primary" href="#contact">Talk to us <svg class="i"><use href="#i-arrow"/></svg></a>
          <a class="btn btn--ghost" href="#what-we-do">What we do</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="what-we-do">
    <div class="wrap">
      <div class="section-head center reveal">
        <span class="eyebrow">What we do</span>
        <h2>{s["name"]} services</h2>
      </div>
      <div class="industries">
{chr(10).join(f'        <div class="ind reveal"><h3>{t}</h3><p>{d}</p></div>' for t, d in s["offer"])}
      </div>
    </div>
  </section>

  <section class="section section--soft">
    <div class="wrap">
      <div class="section-head center reveal">
        <span class="eyebrow">How we work</span>
        <h2>Simple, clear and accountable</h2>
      </div>
      <ol class="process">
{chr(10).join(f'        <li class="reveal"><b>{t}</b><span>{d}</span></li>' for t, d in STEPS)}
      </ol>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head center reveal">
        <span class="eyebrow">More from BTree</span>
        <h2>Other services</h2>
      </div>
      <div class="svc-grid">
{chr(10).join(svc_card(r, o, compact=True) for o in others)}
      </div>
    </div>
  </section>
'''
    page += contact(r, f"Talk to us about {s['name'].lower() if not s['name'].startswith(('Microsoft', 'AWS', 'AI')) else s['name']}",
                    "Tell us where you are today and where you want to be. We will suggest a practical next step, with no obligation.", s["name"])
    page += footer(r)
    out = ROOT / "services" / s["slug"] / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")

# ---------- Privacy notice ----------
PRIVACY_UPDATED = "20 November 2026"
r = "../"
pv = head(r, "Privacy notice | BTree", "How BTree collects, uses and protects personal information, including enquiries sent through our contact form.", SITE + "privacy/",
          ld=[breadcrumbs(("Privacy notice", SITE + "privacy/"))])
pv += nav(r) + f'''
<main id="top">
  <section class="hero hero--page">
    <div class="wrap">
      <div class="hero__copy">
        <nav class="crumbs" aria-label="Breadcrumb"><a href="{r}">Home</a> <span>/</span> Privacy notice</nav>
        <h1>Privacy notice</h1>
        <p class="hero__sub">How we collect, use and protect your personal information. Last updated {PRIVACY_UPDATED}.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap legal">
      <h2>Who we are</h2>
      <p>This website (btree.uk, including the ShiftFlow pages) is run by {COMPANY["name"]}, trading as BTree, a company registered in England and Wales with company number {COMPANY["number"]}. We are based in {COMPANY["location"]}.</p>
      <p>We are the controller of the personal information described in this notice. If you have any questions about it, email us at <a href="mailto:info@btree.uk">info@btree.uk</a>.</p>

      <h2>What we collect</h2>
      <p><b>When you send us an enquiry</b> through the contact form, we collect your name, email address and message, and, if you choose to give them, your company name and phone number. We also record which service you asked about, the page you sent the form from, the date and time, and the country your request came from (worked out by Cloudflare from your connection). We do not store your IP address with your enquiry.</p>
      <p><b>When you email us</b>, we receive your email address, your message and anything else you choose to include.</p>
      <p><b>When you visit the site</b>, our hosting and security providers process technical information such as your IP address and browser type so they can deliver the pages and protect the site from abuse. We do not use analytics, advertising or tracking cookies. If you close the privacy banner, your browser remembers that on your device so it does not appear again; this is never sent to us.</p>

      <h2>How we use it, and our lawful basis</h2>
      <ul>
        <li>To reply to your enquiry and, if you ask, to give you a quote, demo or proposal. This is in our legitimate interests in responding to people who contact us, or is a step you have asked us to take before entering into a contract.</li>
        <li>To keep the contact form free from spam and abuse. This is in our legitimate interests in keeping our services secure.</li>
        <li>To keep a record of our communications with you. This is in our legitimate interests in running our business.</li>
      </ul>
      <p>We will not add you to a marketing list or send you newsletters unless you ask us to, and we never sell your information.</p>

      <h2>Who we share it with</h2>
      <p>We use a small number of trusted service providers who process information on our behalf, under contracts that require them to keep it secure:</p>
      <ul>
        <li><b>Cloudflare</b>, which runs our contact form service and stores enquiries, and provides Turnstile, the check that stops automated spam.</li>
        <li><b>Microsoft</b>, which provides our email (Microsoft 365). Enquiries are sent to our team by email.</li>
        <li><b>GitHub</b>, which hosts this website.</li>
        <li><b>Google Fonts</b>, which supplies the typeface used on this site. Your browser requests the font directly from Google, which receives your IP address.</li>
      </ul>
      <p>We may also share information if the law requires it, or to protect our rights or the safety of others.</p>

      <h2>International transfers</h2>
      <p>Some of these providers process information outside the UK, including in the United States. Where they do, the transfer is protected by UK adequacy regulations (such as the UK-US data bridge) or by the International Data Transfer Agreement or Addendum approved by the Information Commissioner.</p>

      <h2>How long we keep it</h2>
      <p>We keep enquiries sent through the contact form for 24 months, after which they are deleted automatically. If you become a customer, we keep the information we need for our working relationship for as long as that relationship lasts and for up to 6 years afterwards, to meet our legal and accounting obligations.</p>

      <h2>Your rights</h2>
      <p>Under UK data protection law you have the right to:</p>
      <ul>
        <li>ask for a copy of the personal information we hold about you;</li>
        <li>ask us to correct information that is wrong or incomplete;</li>
        <li>ask us to delete your information;</li>
        <li>ask us to restrict how we use it, or object to us using it;</li>
        <li>ask us to transfer it to you or to another organisation.</li>
      </ul>
      <p>To use any of these rights, email <a href="mailto:info@btree.uk">info@btree.uk</a>. We will reply within one month. There is normally no charge.</p>

      <h2>Complaints</h2>
      <p>If you are unhappy with how we have handled your information, please tell us first so we can put it right. You also have the right to complain to the Information Commissioner's Office (ICO) at <a href="https://ico.org.uk/make-a-complaint/" rel="noopener">ico.org.uk</a> or on 0303 123 1113.</p>

      <h2>ShiftFlow app users</h2>
      <p>This notice covers this website and enquiries sent to us. If your employer uses ShiftFlow, your employer is responsible for the staff information held in it, and its own privacy notice explains how that information is used.</p>

      <h2>Changes to this notice</h2>
      <p>We may update this notice from time to time. The date at the top shows when it last changed.</p>
    </div>
  </section>
''' + footer(r)
out = ROOT / "privacy" / "index.html"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(pv, encoding="utf-8")

# ---------- ShiftFlow: the shift-worker journey (replaces the old feature list) ----------
# Every ShiftFlow feature, mapped to a stop on the journey from hiring to leaving, plus the
# things that run in the background all the time. Written into shiftflow/index.html between
# the <!-- journey --> markers.
JOURNEY = [
    ("hire", "i-plus", "Hire", "Say hello. The paperwork is done before day one.", [
        "New starter link with a form you configure",
        "Right to Work checks, with expiry reminders at 30, 14 and 7 days",
        "Contract templates that fill in the employee's details",
        "Contracts and policies signed online, with countersigning",
        "Hourly, salaried and zero hours contracts",
        "Several positions per person, each with its own pay rate",
        "Import your staff list from your previous HR system",
        "Employee number formats and consistent name capitalisation",
    ]),
    ("onboard", "i-users", "Onboard", "Day one, sorted. Everyone knows who is who.", [
        "Profiles for personal, employment, pay, bank, immigration, notes and history",
        "Six directory views: list, classic list, grid, people and profile, org chart and team by location map",
        "Reporting lines, edited by dragging on the org chart",
        "Staff with a home site and extra sites they can work at",
        "Send a document for signature to a whole site or position",
        "Encrypted document library with folders and document types",
        "Document expiry warnings",
        "Sign in by emailed code, with Face ID lock",
        "Read and sign documents, upload evidence",
        "Update personal details, approved by a manager",
    ]),
    ("plan", "i-calendar", "Plan", "Build next week in minutes, not on a Sunday night.", [
        "Week, day, month and coverage heatmap views",
        "Comfortable or Compact density",
        "Drag and drop, resize and drag-create shifts",
        "Shift templates, copy last week or start from scratch",
        "Group by position, category, person or day part",
        "Live hours, cost, wage percentage and sales per labour hour",
        "Weather forecast on every day",
        "Draft, approval and publish workflow",
        "Amend after publishing, notifying only changed shifts",
        "Past days locked against edits",
        "Staff availability shown on the rota",
        "Rota acknowledgement by staff",
        "Print as graphical, table or roster",
        "Double bookings across sites blocked and explained",
        "Settings set once for the business, overridden per site",
        "Trading days that run past midnight",
    ]),
    ("work", "i-clock", "Work", "Clock in, crack on. Cover sorts itself out.", [
        "Tablet kiosk with PIN clock-in, breaks and clock-out",
        "Kiosk cards, list or search view, in two densities",
        "Works offline and syncs when back online",
        "Optional photo on clock-in, and geofencing",
        "Late, early leave and no-show rules you can tune",
        "Manager overrides with a reason and audit record",
        "Shifts, hours worked and holiday at a glance",
        "Set availability",
        "Pick up open shifts and offer swaps",
        "Open shifts broadcast across sites, claimed by staff",
        "Shift swaps and giveaways, approved by managers",
        "Transfers between sites with an audit trail",
    ]),
    ("rest", "i-plane", "Rest", "Time off, without the back-and-forth.", [
        "Request time off, even when offline",
        "Absence types, entitlements and leave years",
        "Allowances, carry-over and blackout dates",
        "UK bank holidays",
        "Sickness recording",
        "Leave shown on the rota and checked for clashes",
        "Requests approved from one inbox",
    ]),
    ("pay", "i-chart", "Pay", "Pay people right, and see the whole picture.", [
        "Unscheduled clock-ins approved into the timesheet",
        "Day and week timesheets, planned against actual",
        "Approve a whole week in one click",
        "Missed clock-out sweep",
        "Timesheets and wage costs",
        "Pay run export for payroll",
        "Sales against labour",
        "Attendance and overtime",
        "Coverage heatmap",
        "Compliance breaches",
        "Leave summary",
        "Right to Work status",
        "Print and CSV export on every report",
        "Dashboard with sales, labour, compliance and who is on shift now",
    ]),
    ("leave", "i-history", "Leave", "Goodbyes done properly, and a warm welcome back.", [
        "Leavers and rehires with dated history",
        "Session timeouts you set, and sign out everywhere",
        "People insights: headcount, contracts, service and turnover",
    ]),
]
ALWAYS_ON = [
    ("i-landmark", "UK compliance", "Checked on every shift, before you publish.", [
        "11 hours rest between shifts",
        "48 hour average working week",
        "Minimum breaks",
        "Daily hours and night work limits for under-18s",
        "Food hygiene and management certificates by position",
        "Visa weekly hour caps from Right to Work, across all sites",
        "Leave clashes and overlapping shifts",
        "Errors block publishing, warnings are shown",
    ]),
    ("i-megaphone", "Communication", "Everyone in the loop, nobody spammed.", [
        "Announcements to a site or position, with who has read them",
        "Announcements with read confirmation",
        "In-app notifications and an approvals inbox",
        "Rota emails with calendar attachments",
        "Quiet hours and batching for rota emails",
        "Birthday emails and automatic reminders",
        "Your own email templates and email server",
    ]),
    ("i-shield", "Security and administration", "Locked down, without locking people out.", [
        "Single sign-on with Microsoft Entra ID or any OIDC provider",
        "Authenticator app MFA with recovery codes",
        "Roles from fine-grained permissions, scoped to sites",
        "Full audit log of every change",
        "Encrypted sensitive data with key rotation",
        "One login across several businesses",
        "You choose which parts each site offers",
        "Twelve colour themes, light and dark",
    ]),
]


def journey_html():
    import html as _h
    esc = _h.escape
    total = sum(len(j[4]) for j in JOURNEY) + sum(len(a[3]) for a in ALWAYS_ON)
    n = len(JOURNEY)
    stops = "\n".join(
        f'''          <button class="jstop" type="button" role="tab" id="jtab-{sid}" aria-controls="jpanel-{sid}" aria-selected="{"true" if i == 0 else "false"}" tabindex="{0 if i == 0 else -1}">
            <span class="jstop__dot"><svg class="i"><use href="#{ico}"/></svg></span>
            <span class="jstop__num">{i + 1:02d}</span><span class="jstop__name">{name}</span><span class="jstop__hits" aria-hidden="true"></span>
          </button>''' for i, (sid, ico, name, tag, feats) in enumerate(JOURNEY))
    panels = "\n".join(
        f'''        <div class="jpanel{" is-active" if i == 0 else ""}" id="jpanel-{sid}" role="tabpanel" aria-labelledby="jtab-{sid}">
          <div class="jpanel__head">
            <span class="jpanel__stop">Stop {i + 1:02d} of {n:02d}</span>
            <h3><svg class="i"><use href="#{ico}"/></svg>{name}</h3>
            <p class="jpanel__tag">{esc(tag)}</p>
          </div>
          <ul class="jfeat">
{chr(10).join(f'            <li>{esc(f)}</li>' for f in feats)}
          </ul>
        </div>''' for i, (sid, ico, name, tag, feats) in enumerate(JOURNEY))
    always = "\n".join(
        f'''          <article class="jbg">
            <h4><span class="jbg__ico"><svg class="i"><use href="#{ico}"/></svg></span>{name}</h4>
            <p class="jbg__tag">{esc(tag)}</p>
            <ul class="jfeat jfeat--compact">
{chr(10).join(f'              <li>{esc(f)}</li>' for f in feats)}
            </ul>
          </article>''' for ico, name, tag, feats in ALWAYS_ON)
    return f'''<section class="section journey" id="all-features">
    <div class="wrap">
      <div class="section-head center reveal">
        <span class="eyebrow">Everything in ShiftFlow</span>
        <h2>From first hello to <span class="grad">fond farewell</span></h2>
        <p class="lead">All {total} features, mapped to the moments that matter in a shift worker's life. Pick a stop on the line, or search for anything.</p>
      </div>
      <div class="jsearch">
        <svg class="i" viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
        <input type="search" id="jsearch" placeholder="Search {total} features: try offline, Right to Work or swap" aria-label="Search ShiftFlow features" autocomplete="off" />
        <span class="jsearch__count" aria-live="polite"></span>
      </div>
      <div class="jmap">
        <div class="jline" role="tablist" aria-label="The shift-worker journey">
          <span class="jline__track" aria-hidden="true"><span class="jline__fill"></span><span class="jline__train"></span></span>
{stops}
        </div>
        <div class="jpanels">
{panels}
        </div>
        <p class="jempty" hidden>Nothing matches that yet. Try another word, or <a href="#contact">ask us</a> whether ShiftFlow can do it.</p>
      </div>
      <div class="jalways">
        <p class="jalways__title"><span class="jlive" aria-hidden="true"></span>Always running in the background</p>
        <div class="jalways__grid">
{always}
        </div>
      </div>
    </div>
  </section>'''


# ---------- ShiftFlow: industries as live 24-hour shift maps ----------
# Typical shift patterns per industry (hours on a 24-hour clock; an end past 24 runs past midnight).
SF_ICONS = {
    "cup": '<path d="M17 8h1a4 4 0 0 1 0 8h-1"/><path d="M3 8h14v9a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4z"/><path d="M6 2v2M10 2v2M14 2v2"/>',
    "bag": '<path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/>',
    "heart": '<path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7z"/><path d="M3.2 12h4.3l1.5-3 3 6 1.5-3h7.3"/>',
    "truck": '<path d="M14 18V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2"/><path d="M15 18H9"/><path d="M19 18h2a1 1 0 0 0 1-1v-3.65a1 1 0 0 0-.22-.62l-3.48-4.35A1 1 0 0 0 17.52 8H14"/><circle cx="17" cy="18" r="2"/><circle cx="7" cy="18" r="2"/>',
    "factory": '<path d="M2 20a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8l-7 5V8l-7 5V4a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2z"/><path d="M17 18h1M12 18h1M7 18h1"/>',
    "building": '<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4M8 6h.01M12 6h.01M16 6h.01M8 10h.01M12 10h.01M16 10h.01M8 14h.01M12 14h.01M16 14h.01"/>',
}
SF_INDUSTRIES = [
    ("Hospitality", "cup", "#f59e0b",
     "Restaurants, bars, cafes, bakeries and hotels. Late finishes, split shifts and busy weekends.",
     [("Lunch", 10, 15), ("Evening", 17, 25), ("Close", 20, 26)]),
    ("Retail", "bag", "#ec4899",
     "Shops and multi-site chains. Cover for opening hours, seasonal peaks and Sunday trading.",
     [("Open", 7, 15), ("Mid", 10, 18), ("Close", 14, 22)]),
    ("Health and social care", "heart", "#ef4444",
     "Care homes and home care. Round-the-clock rotas, night shifts and training that must stay in date.",
     [("Early", 7, 15), ("Late", 15, 23), ("Night", 23, 31)]),
    ("Warehousing and logistics", "truck", "#0ea5e9",
     "Distribution centres and delivery teams. Rotating shifts, agency cover and accurate clock-ins.",
     [("Days", 6, 14), ("Backs", 14, 22), ("Nights", 22, 30)]),
    ("Manufacturing", "factory", "#8b5cf6",
     "Production lines and plants. Shift patterns, overtime and Working Time limits checked for you.",
     [("Days", 6, 18), ("Nights", 18, 30)]),
    ("Facilities, cleaning and security", "building", "#10b981",
     "Teams spread across client sites. Know who is on site, and pay only for hours worked.",
     [("Clean", 5, 9), ("Clean", 18, 22), ("Security", 19, 31)]),
]


def industries_html():
    def hh(h):
        return f"{int(h) % 24:02d}:00"
    cards = []
    for name, icon, colour, desc, shifts in SF_INDUSTRIES:
        lanes = []
        for i, (label, s, e) in enumerate(shifts):
            title = f"{label}, {hh(s)} to {hh(e)}"
            segs = [(s, min(e, 24))]
            if e > 24:
                segs.append((0, e - 24))
            longest = max(range(len(segs)), key=lambda k: segs[k][1] - segs[k][0])  # label the bigger piece
            segs = [(a, b, k == longest) for k, (a, b) in enumerate(segs)]
            bars = "".join(
                f'<span class="shiftmap__bar" style="--s:{a};--e:{b};--i:{i}" title="{title}">{label if first else ""}</span>'
                for a, b, first in segs)
            lanes.append(f'<div class="shiftmap__lane">{bars}</div>')
        data = ",".join(f"{s}-{e}" for _, s, e in shifts)
        cards.append(f'''        <article class="ind2 reveal" style="--c:{colour}" data-shifts="{data}">
          <div class="ind2__top">
            <span class="ind2__ico"><svg class="i" viewBox="0 0 24 24" aria-hidden="true">{SF_ICONS[icon]}</svg></span>
            <h3>{name}</h3>
          </div>
          <p>{desc}</p>
          <div class="shiftmap" aria-hidden="true">
            {"".join(lanes)}
            <span class="shiftmap__now"></span>
            <div class="shiftmap__ticks"><span>00</span><span>06</span><span>12</span><span>18</span><span>24</span></div>
          </div>
          <p class="ind2__live"><span class="ind2__dot"></span><span class="ind2__count">Typical shifts across a day</span></p>
        </article>''')
    return '''<section class="section" id="industries">
    <div class="wrap">
      <div class="section-head center reveal">
        <span class="eyebrow">Industries</span>
        <h2>Built for every team that works in shifts</h2>
        <p class="lead">ShiftFlow started in hospitality, where shifts are at their most complicated. The same rota, time clock and HR tools work for any business with hourly staff across one site or many.</p>
        <p class="ind2__clock" hidden><span class="ind2__dot"></span><span>It is <b class="ind2__time">--:--</b> in the UK. Here is who is on shift right now.</span></p>
      </div>
      <div class="industries industries--live">
''' + "\n".join(cards) + '''
      </div>
      <p class="ind2__note">Typical shift patterns on a 24-hour clock. Yours will look different, and ShiftFlow handles that too.</p>
    </div>
  </section>'''


# ---------- ShiftFlow page: same form, between the contact-form markers ----------
sf_path = ROOT / "shiftflow/index.html"
sf_text = sf_path.read_text(encoding="utf-8")
start, end = "<!-- contact-form -->", "<!-- /contact-form -->"
a, b = sf_text.index(start) + len(start), sf_text.index(end)
sf_text = sf_text[:a] + "\n        " + contact_form("../", "ShiftFlow", "Book a demo") + "\n        " + sf_text[b:]
sf_text = re.sub(r'assets/css/site\.css(\?v=\w+)?"', f'assets/css/site.css?v={CSS_V}"', sf_text)
SF_URL = SITE + "shiftflow/"
SF_DESC = "Rotas, time and attendance and HR for UK shift-based teams, in one flow."
start, end = "<!-- seo -->", "<!-- /seo -->"
a, b = sf_text.index(start) + len(start), sf_text.index(end)
sf_text = sf_text[:a] + "\n" + seo_tags("../", "ShiftFlow by BTree", SF_DESC, SF_URL, image="shiftflow.png",
    image_alt="ShiftFlow: rotas, clock-ins and HR in one flow", icon="shiftflow", ld=[
        {"@type": "SoftwareApplication", "name": "ShiftFlow", "url": SF_URL, "description": SF_DESC,
         "applicationCategory": "BusinessApplication", "operatingSystem": "Web, iOS, Android",
         "image": SITE + "assets/og/shiftflow.png", "publisher": {"@id": ORG_ID}},
        breadcrumbs(("ShiftFlow", SF_URL))]) + "  " + sf_text[b:]
sf_text = re.sub(r'assets/js/site\.js(\?v=\w+)?"', f'assets/js/site.js?v={JS_V}"', sf_text)
sf_text = re.sub(r'(<span>&copy; <span id="year">\d{4}</span> \{btree\}\. All rights reserved\.)(?: <span class="footer__legal">[^<]*</span>)?(</span>)',
                 lambda m: f'{m.group(1)} <span class="footer__legal">{COMPANY_LINE}</span>{m.group(2)}', sf_text)
start, end = "<!-- journey -->", "<!-- /journey -->"
a, b = sf_text.index(start) + len(start), sf_text.index(end)
sf_text = sf_text[:a] + "\n  " + journey_html() + "\n  " + sf_text[b:]
start, end = "<!-- partners -->", "<!-- /partners -->"
a, b = sf_text.index(start) + len(start), sf_text.index(end)
sf_text = sf_text[:a] + "\n  " + partners_html("../") + "\n  " + sf_text[b:]
# Same footer as every other page: replace everything from </main> to the end.
sf_text = sf_text[:sf_text.index("\n</main>")] + footer("../")
start, end = "<!-- industries -->", "<!-- /industries -->"
a, b = sf_text.index(start) + len(start), sf_text.index(end)
sf_text = sf_text[:a] + "\n  " + industries_html() + "\n  " + sf_text[b:]
sf_path.write_text(sf_text, encoding="utf-8", newline="\r\n")

# ---------- 404 ----------
# GitHub Pages serves this for any missing URL, at any depth, so every link is root-absolute.
r = "/"
nf = head(r, "Page not found | BTree", "The page you were looking for could not be found.", SITE, noindex=True)
NF_LINES = [
    '<span class="t-p">$</span> curl -I https://btree.uk<span class="nf__path">/this-page</span>',
    'HTTP/2 <b class="t-bad">404 Not Found</b>',
    '',
    '<span class="t-p">$</span> btree diagnose --everything',
    '<span class="t-dim">[</span><span class="t-ok">&nbsp;OK&nbsp;</span><span class="t-dim">]</span> network     <span class="t-dim">online</span>',
    '<span class="t-dim">[</span><span class="t-ok">&nbsp;OK&nbsp;</span><span class="t-dim">]</span> firewall    <span class="t-dim">holding the line</span>',
    '<span class="t-dim">[</span><span class="t-ok">&nbsp;OK&nbsp;</span><span class="t-dim">]</span> dns         <span class="t-dim">resolving</span>',
    '<span class="t-dim">[</span><span class="t-ok">&nbsp;OK&nbsp;</span><span class="t-dim">]</span> coffee      <span class="t-dim">freshly brewed</span>',
    '<span class="t-dim">[</span><span class="t-bad">FAIL</span><span class="t-dim">]</span> this page   <span class="t-bad">gone walkabout</span>',
    '',
    '<span class="t-p">$</span> <span class="term__cursor"></span>',
]
nf_term = "".join(f'<span class="ln" style="--d:{i}">{line or "&nbsp;"}</span>' for i, line in enumerate(NF_LINES))
nf += nav(r).replace('href="#contact"', 'href="/#contact"') + '''
<main id="top">
  <section class="hero nf">
    <div class="wrap nf__grid">
      <div class="nf__copy">
        <div class="nf__code" data-text="{404}" aria-hidden="true">{404}</div>
        <span class="eyebrow">Error 404 &middot; Page not found</span>
        <h1>Well, this is <span class="grad">broken.</span></h1>
        <p class="hero__sub">We checked the network, the firewall and the coffee machine. Everything is working except this page, which seems to have wandered off. It may have moved when we reorganised the site.</p>
        <div class="hero__actions">
          <a class="btn btn--primary" href="/">Take me home <svg class="i"><use href="#i-arrow"/></svg></a>
          <a class="btn btn--ghost" href="/#services">Explore our services</a>
        </div>
        <p class="nf__links">Or try <a href="/shiftflow/">ShiftFlow</a>, <a href="/#contact">get in touch</a>, or tell us about the broken link at <a href="mailto:info@btree.uk?subject=Broken%20link%20on%20btree.uk">info@btree.uk</a>.</p>
      </div>
      <div class="term" role="img" aria-label="A terminal running diagnostics: the network, firewall, DNS and coffee are all fine, but the page cannot be found.">
        <div class="term__bar" aria-hidden="true"><i></i><i></i><i></i><span>btree@diagnostics: ~</span></div>
        <pre class="term__out" aria-hidden="true"><code>''' + nf_term + '''</code></pre>
      </div>
    </div>
  </section>
  <script>
    // Show the address the visitor actually tried (as text, never as HTML).
    (function () {
      var p = document.querySelector('.nf__path');
      if (p && location.pathname !== '/404.html') p.textContent = decodeURI(location.pathname).slice(0, 60);
    })();
  </script>
''' + footer(r)
(ROOT / "404.html").write_text(nf, encoding="utf-8")

# ---------- Sitemap ----------
import subprocess, datetime


def lastmod(path):
    """Date the page last changed: today if it has uncommitted changes, else its last commit date."""
    def git(*args):
        try:
            return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, timeout=10).stdout.strip()
        except (OSError, subprocess.SubprocessError):
            return ""
    if git("status", "--porcelain", "--", path):
        return datetime.date.today().isoformat()
    return git("log", "-1", "--format=%cs", "--", path) or datetime.date.today().isoformat()


pages = [(SITE, "index.html"), (SITE + "shiftflow/", "shiftflow/index.html")] + \
        [(f"{SITE}services/{s['slug']}/", f"services/{s['slug']}/index.html") for s in SERVICES] + \
        [(SITE + "privacy/", "privacy/index.html")]
urls = [u for u, _ in pages]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for u, f in pages:
    sm += f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{lastmod(f)}</lastmod>\n  </url>\n"
sm += "</urlset>\n"
(ROOT / "sitemap.xml").write_text(sm, encoding="utf-8")
print("built", len(urls), "pages")
