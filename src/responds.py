from http import cookies

def respond_200(path, msg, content_type="text/plain"):
    aaa = msg.encode()
    path.send_response(200)
    path.send_header("Content-type", content_type)
    path.send_header("Content-Length", str(len(aaa)))
    path.end_headers()

    path.wfile.write(aaa)


def respond_404(self):
    msg = "File not found. Try searching elsewhere"
    self.send_response(404)
    self.send_header("Content-type", 'text/plain')
    self.send_header("Content-Length", str(len(msg)))
    self.end_headers()

    self.wfile.write(msg.encode())


def respond_405(self):  # ответ серверу об ошибке 405
    msg = "Method Not Allowed!"
    self.send_response(405)
    self.send_header("Content-type", 'text/plain')
    self.send_header("Content-Length", str(len(msg)))
    self.end_headers()

    self.wfile.write(msg.encode())

def respond_500(self):  # ответ серверу об ошибке 500
    msg = "Method Not Allowed!"
    self.send_response(500)
    self.send_header("Content-type", 'text/plain')
    self.send_header("Content-Length", str(len(msg)))
    self.end_headers()

    self.wfile.write(msg.encode())

def respond_302(self, redirect,cookie):
    respond(self, "", 302, "text/plain", redirect, cookie)

def respond(self, msg, status_code, content_type="text/plain", redirect="", cookie=""):
    self.send_response(status_code)
    self.send_header("Content-type", content_type)
    self.send_header("Content-length", str(len(msg)))
    self.send_header("Location", redirect)
    self.send_header("Set-Cookie", cookie)
    self.end_headers()

    if isinstance(msg, str):
        msg = msg.encode()
    self.wfile.write(msg)

