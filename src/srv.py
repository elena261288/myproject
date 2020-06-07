import socketserver
import os
from http.server import SimpleHTTPRequestHandler
from urllib.parse import parse_qs

PORT = int(os.getenv("PORT", 8000))
print(f"port = {PORT}")

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/hello"):
            path, qs = self.path.split("?")
            qs = parse_qs(qs)
            age = qs["age"][0]
            born = str(2020 - int(age))
            msg = f"""
                Hello, dear!
                You were born in the {born} year
                """

            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.send_header("Content-Length", len(msg))
            self.end_headers()

            self.wfile.write(msg.encode())
        else:
            return SimpleHTTPRequestHandler.do_GET(self)



with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("it works")
    httpd.serve_forever()
