"""Local preview server for the site, behaving like GitHub Pages for missing pages.

Python's built-in server shows its own plain error page; this one serves 404.html instead,
so the preview matches btree.uk. Run from the repo root:

    python tools/serve.py          # http://localhost:8000
    python tools/serve.py 8080     # another port
"""
import http.server
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def list_directory(self, path):
        # GitHub Pages never lists folders; treat a folder without index.html as missing.
        self.send_error(404)
        return None

    def send_error(self, code, message=None, explain=None):
        page = ROOT / "404.html"
        if code == 404 and page.exists():
            body = page.read_bytes()
            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            if self.command != "HEAD":
                self.wfile.write(body)
            return
        super().send_error(code, message, explain)


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    with http.server.ThreadingHTTPServer(("127.0.0.1", port), Handler) as httpd:
        print(f"Serving {ROOT} at http://localhost:{port}/ (Ctrl+C to stop)")
        httpd.serve_forever()
