from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"message": "Salam rodnoi", "path": self.path}).encode())

HTTPServer(("127.0.0.1", 6767), Handler).serve_forever()
