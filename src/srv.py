import socketserver
import os
from http.server import SimpleHTTPRequestHandler
from urllib.parse import parse_qs
from datetime import datetime
from pathlib import Path

PORT = int(os.getenv("PORT", 8000))  # задает адрес нашего локал хоста
print(f"port = {PORT}")

MYPROJECT_DIR = Path(__file__).parent.parent.resolve()
print(f"{MYPROJECT_DIR=}")

PAGES_DIR = MYPROJECT_DIR/"pages"
print(f"{PAGES_DIR=}")

class NotFound(Exception):
    pass

class MethodNotAllowed(Exception):
    pass

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.extract_path()
        handlers = {
            "hello": self.handler_hello,
            "goodbye": self.handler_goodbye,
            "skills": self.handler_skills,
            "education": self.handler_education,
            "job": self.handler_job
        }
        default_handler = super().do_GET
        #if path is not handlers:
        #    print("is not found file")
        #handler = handlers[path]
        handler = handlers.get(path, default_handler)
        try:
            handler()
        except NotFound:
            self.respond_404()
        except MethodNotAllowed:
            self.respond_405()


    #def do_GET(self):
       # try:
       #     self.do("get")
       # except:                 #???
        #    super().do_GET()

    #def do_POST(self):
    #    try:
    #        self.do("post")
      #  except:                 #???
       #     super().do_POST()



    def handler_skills(self):
        html = PAGES_DIR/"skills"/"index.html"
        content = self.get_content(html)
        self.respond(content, "text/html")

    def get_content(self, fp):
        if not fp.is_file():
            raise NotFound

        with fp.open('r') as src:
            con = src.read()

        return con



    def handler_education(self):
        html = PAGES_DIR / "education" / "index.html"
        content = self.get_content(html)
        self.respond(content, "text/html")

    def handler_job(self):
        html = PAGES_DIR / "job" / "index.html"
        content = self.get_content(html)
        self.respond(content, "text/html")

    def handler_goodbye(self):
        time = datetime.now().hour
        parting = 'day' if time in range(9, 19) else 'night'
        msg = f'Good {parting}!'

        self.respond(msg, "text/plain")

    def handler_hello(self): #вытягиваем имя и возраст в хелло, сообщение
        args = self.build_query_args()
        name = self.build_name(args) #args.get("name", "dear")  #достать из словаря по ключу "имя"
        age = self.build_age(args) #args.get("age")    #дастать из словаря значение по ключу "возраст"

        msg = f'Hello, {name}!'

        if age:
            nowy = datetime.now().year
            year = nowy - int(age)
            msg += f'\n You was born at {year}!'

        self.respond(msg, "text/plain")

    def build_name(self, query_args):
        return query_args.get("name", "Dear")

    def build_age(self, query_args):
        return query_args.get("age")

    #def resp(self, msg, mistake,content_type="text/plain"):
     #   self.send_response(mistake)
      #  self.send_header("Content-type", content_type)
      #  self.send_header("Content-Length", str(len(msg)))
     #   self.end_headers()

     #   self.wfile.write(msg.encode())

    def respond(self, msg, content_type="text/plain"):
        self.send_response(200)
        self.send_header("Content-type", content_type)
        self.send_header("Content-Length", str(len(msg)))
        self.end_headers()

        self.wfile.write(msg.encode())

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

    def build_query_args(self): #разбиваем qs на словарь qs
        _path, *qs = self.path.split('?')
        args = {}

        if len(qs) != 1:
            return args

        qs = qs[0] #преобразовали из списка в строку
        qs = parse_qs(qs)

        for key, value in qs.items(): # для каждого картежа "ключ-знач" выполнить...
            if not value:
                continue
            args[key] = value[0]
        return args

    def extract_path(self): #выделяем из всего пути начало
        path = self.path.split('/')[1]
        path = path.split("?")[0]
        return path.split("#")[0]
        #patha, *_qs = self.path.split('?')
        #pathb, *_qs = patha.split('#')
        #if pathb[-1] == '/':
         #   path = pathb[:-1]
        #return path


with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("it works")
    httpd.serve_forever()
