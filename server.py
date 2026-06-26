import http.server, os
BASE = os.path.dirname(os.path.abspath(__file__))
class H(http.server.BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.end_headers()
    def do_GET(self):
        path = self.path.split('?')[0].lstrip('/')
        if path in ('', '/'): self._serve('index.html', 'text/html; charset=utf-8')
        elif path == 'logo.svg': self._serve('logo.svg', 'image/svg+xml', binary=True)
        else: self.send_response(404); self.end_headers()
    def _serve(self, fn, ct, binary=False):
        try:
            with open(os.path.join(BASE, fn), 'rb' if binary else 'r', encoding=None if binary else 'utf-8') as f: c = f.read()
            self.send_response(200); self.send_header('Content-Type', ct); self.end_headers()
            self.wfile.write(c if isinstance(c, bytes) else c.encode('utf-8'))
        except: self.send_response(404); self.end_headers()
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    print(f"BETPOWO : http://0.0.0.0:{port}")
    http.server.HTTPServer(('0.0.0.0', port), H).serve_forever()
