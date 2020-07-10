from http import cookies


def respond_200(path, msg, content_type="text/plain"):
    aaa = msg.encode()
    path.send_response(200)
    path.send_header("Content-type", content_type)
    path.send_header("Content-Length", str(len(aaa)))
    path.end_headers()

    path.wfile.write(aaa)


def respond_404(server):
    msg = "File not found. Try searching elsewhere"
    server.send_response(404)
    server.send_header("Content-type", "text/plain")
    server.send_header("Content-Length", str(len(msg)))
    server.end_headers()

    server.wfile.write(msg.encode())


def respond_405(srv):  # ответ серверу об ошибке 405
    msg = "Method Not Allowed!"
    srv.send_response(405)
    srv.send_header("Content-type", "text/plain")
    srv.send_header("Content-Length", str(len(msg)))
    srv.end_headers()

    srv.wfile.write(msg.encode())


def respond_500(srv, exc=""):  # ответ серверу об ошибке 500
    msg = f"""
    <h1>Internal Server Error</h1>
    <hr>
    <pre>
    {exc}
    </pre>
    <hr>
    """
    srv.send_response(500)
    srv.send_header("Content-type", "text/html")
    srv.send_header("Content-Length", str(len(msg)))
    srv.end_headers()

    srv.wfile.write(msg.encode())


def respond_302(server, redirect, cookie):
    respond(server, "", 302, "text/plain", redirect, cookie)


def respond(srv, msg, status_code, content_type="text/plain", redirect="", cookie=""):
    srv.send_response(status_code)
    srv.send_header("Content-type", content_type)
    srv.send_header("Content-length", str(len(msg)))
    srv.send_header("Location", redirect)
    srv.send_header("Set-Cookie", cookie)
    srv.end_headers()

    if isinstance(msg, str):
        msg = msg.encode()
    srv.wfile.write(msg)
