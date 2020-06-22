import socketserver
import os
from http.server import SimpleHTTPRequestHandler
from urllib.parse import parse_qs
from datetime import datetime

PORT = int(os.getenv("PORT", 8000))  # задает адрес нашего локал хоста
print(f"port = {PORT}")

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.extract_path()
        handlers = {
            "hello": self.handler_hello,
            "goodbye": self.handler_goodbye
        }
        default_handler = super().do_GET()

        handler = handlers.get(path, default_handler)
        handler()

    def handler_goodbye(self):
        time = datetime.now().hour
        parting = 'day' if time in range(9, 19) else 'night'
        msg = f'Good {parting}!'

        self.respond(msg)

    def handler_hello(self): #вытягиваем имя и возраст в хелло, сообщение
        args = self.build_query_args()
        name = self.build_name(args) #args.get("name", "dear")  #достать из словаря по ключу "имя"
        age = self.build_age(args) #args.get("age")    #дастать из словаря значение по ключу "возраст"

        msg = f'Hello, {name}!'

        if age:
            nowy = datetime.now().year
            year = nowy - int(age)
            msg += f'\n You was born at {year}!'

        self.respond(msg)

    def build_name(self, query_args):
        return query_args.get("name", "Dear")

    def build_age(self, query_args):
        return query_args.get("age")

    def respond(self, msg): #ответ серверу
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
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

        for key, value in qs.items(): # для каждой сцепки "ключ-знач" выполнить...
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
