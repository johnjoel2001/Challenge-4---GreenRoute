#!/usr/bin/env python3
import http.server
import socketserver
import os
from pathlib import Path

# Serve the built Vite app from demo/dist
DEMO_PATH = Path(__file__).parent / "demo" / "dist"
os.chdir(DEMO_PATH)

PORT = int(os.environ.get("PORT", 8000))

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        super().end_headers()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving {DEMO_PATH} on port {PORT}")
    httpd.serve_forever()
