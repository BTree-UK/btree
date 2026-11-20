-- Contact form enquiries. Apply with:
--   npx wrangler d1 execute btree-contact --remote --file=schema.sql
CREATE TABLE IF NOT EXISTS enquiries (
  id          TEXT PRIMARY KEY,
  created_at  TEXT NOT NULL,              -- ISO 8601, UTC
  name        TEXT NOT NULL,
  email       TEXT NOT NULL,
  company     TEXT NOT NULL DEFAULT '',
  phone       TEXT NOT NULL DEFAULT '',
  service     TEXT NOT NULL DEFAULT '',
  message     TEXT NOT NULL,
  page        TEXT NOT NULL DEFAULT '',   -- page the form was sent from
  country     TEXT NOT NULL DEFAULT '',   -- from Cloudflare; no IP address is stored
  status      TEXT NOT NULL DEFAULT 'new',
  notified    INTEGER NOT NULL DEFAULT 0  -- 1 once the notification email was sent
);
CREATE INDEX IF NOT EXISTS enquiries_created_at ON enquiries (created_at);
CREATE INDEX IF NOT EXISTS enquiries_email ON enquiries (email);
