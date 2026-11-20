# BTree contact form API

A Cloudflare Worker that receives the contact form on btree.uk. It:

1. checks the fields, the hidden honeypot field and Cloudflare Turnstile;
2. stores the enquiry in a Cloudflare D1 database (`btree-contact`, table `enquiries`);
3. emails it to `MAIL_TO` from the `MAIL_FROM` mailbox through Microsoft Graph, with Reply-To set to the sender;
4. deletes enquiries older than 24 months every night, as the privacy notice promises.

The site posts to `https://forms.btree.uk/contact`. Add `?localapi` to a page URL to post to a local Worker (`npm run dev`, `http://localhost:8787/contact`) instead.

## One-off setup

Run everything from this folder (`worker/`).

```sh
npm install
npx wrangler login
```

### 1. Database

```sh
npx wrangler d1 create btree-contact     # copy the database_id into wrangler.toml
npm run db:init                          # creates the enquiries table
```

### 2. Turnstile (spam protection)

Cloudflare dashboard > Turnstile > Add widget:

- Name: `btree.uk contact form`
- Hostnames: `btree.uk`, `www.btree.uk` (keep `localhost` out of the live widget)
- Mode: Managed

Put the **site key** into `TURNSTILE_SITE_KEY` in `tools/build_site.py` and rebuild the site (`python tools/build_site.py .` from the repo root). Store the **secret key** in the Worker:

```sh
npx wrangler secret put TURNSTILE_SECRET
```

### 3. Email through Microsoft 365 (Graph)

In the Entra admin centre > App registrations > New registration (`btree-contact-form`, single tenant):

1. API permissions > Add > Microsoft Graph > **Application** permissions > `Mail.Send` > Grant admin consent.
2. Certificates & secrets > New client secret. Copy the value.
3. Limit the app to the one mailbox it sends from, so it cannot send as anyone else. In Exchange Online PowerShell:

   ```powershell
   New-DistributionGroup -Name "Contact form senders" -Type Security -Members info@btree.uk
   New-ApplicationAccessPolicy -AppId <client-id> -PolicyScopeGroupId "Contact form senders" -AccessRight RestrictAccess -Description "btree-contact Worker"
   ```

Then store the three values:

```sh
npx wrangler secret put MS_TENANT_ID
npx wrangler secret put MS_CLIENT_ID
npx wrangler secret put MS_CLIENT_SECRET
```

`MAIL_FROM` and `MAIL_TO` are in `wrangler.toml`. `MAIL_TO` can be a comma-separated list. If the Graph secrets are missing, enquiries are still stored but no email is sent.

### 4. Deploy

```sh
npm run deploy
```

This publishes the Worker and creates `forms.btree.uk` on your Cloudflare zone automatically.

## Day to day

See recent enquiries:

```sh
npx wrangler d1 execute btree-contact --remote --command "SELECT created_at, name, email, company, service, notified FROM enquiries ORDER BY created_at DESC LIMIT 20"
```

Enquiries with `notified = 0` were stored but the email failed. Check the Worker logs in the Cloudflare dashboard (Workers > btree-contact > Logs).

Delete someone's data on request:

```sh
npx wrangler d1 execute btree-contact --remote --command "DELETE FROM enquiries WHERE email = 'person@example.com'"
```

## Local development

The live Worker and Turnstile widget only accept btree.uk, so local testing uses a local Worker and Cloudflare's test keys. Create `worker/.dev.vars` (gitignored) with:

```sh
TURNSTILE_SECRET=1x0000000000000000000000000000000AA
ALLOWED_ORIGINS=http://localhost:8000,http://127.0.0.1:8000
```

Then:

```sh
npm run db:init:local
npm run dev                     # local Worker on http://localhost:8787
python tools/serve.py           # from the repo root, site on http://localhost:8000
```

Open the site with `?localapi`, for example `http://localhost:8000/?localapi#contact`. The form then posts to the local Worker and uses Cloudflare's always-pass Turnstile test key. Without `?localapi` the form talks to the live API, which rejects localhost.
