import json
import socketserver
from http.server import SimpleHTTPRequestHandler
from urllib.parse import parse_qs
from datetime import datetime
from errors import NotFound, MethodNotAllowed, UnknownPath
from constants import PORT, MYPROJECT_DIR, PAGES_DIR, COUNTER
from responds import respond, respond_404, respond_405, respond_500



print(f"port = {PORT}")
print(f"{MYPROJECT_DIR=}")
print(f"{PAGES_DIR=}")

class MyHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        try:
            self.separation_header("get")
        except UnknownPath:
            respond_404(self)
            #super().do_GET()

    def do_POST(self):
        try:
            self.separation_header("post")
        except UnknownPath:
            respond_404(self)
            #super().do_POST()

    def separation_header(self, method):
        path = self.extract_path()

        handlers = {
            "hello": self.handler_hello,
            "goodbye": self.handler_goodbye,
            "skills": self.handler_skills,
            "education": self.handler_education,
            "job": self.handler_job,
            "": self.handler_index,
            "counter": self.handler_count
        }

        handler = handlers[path]
        try:
            handler(method)
        except NotFound:
            respond_404(self)
        except MethodNotAllowed:
            respond_405(self)
        except Exception:
            respond_500(self)

    def handler_count(self, method):
        json_file = PAGES_DIR / "counter" / "counter.json"
        html_file = PAGES_DIR / "counter" / "index.html"
        job_json = self.load_json_file(json_file)
        cont_html = self.get_content(html_file)
        html = ""
        for page, visits in job_json.items():
            msg = cont_html.format(page=page, visits=visits)
            # msg = json.dumps(job_json, sort_keys=True, indent=4)
            html += msg
        respond(self, html, "text/html")

    def handler_index(self, method):
        self.visits_counter()
        html = MYPROJECT_DIR/"index.html"
        content = self.get_content(html)
        respond(self, content, "text/html")

    def handler_skills(self, method):
        self.visits_counter()
        html = PAGES_DIR/"skills"/"index.html"
        content = self.get_content(html)
        respond(self, "text/html", content)

    def get_content(self, fp):
        if not fp.is_file():
            raise NotFound

        with fp.open('r', encoding='utf-8') as src:
            con = src.read()

        return con

    def handler_education(self, method):
        self.visits_counter()
        html = PAGES_DIR / "education" / "index.html"
        content = self.get_content(html)
        respond(self, content, "text/html")

    def handler_job(self, method):
        self.visits_counter()
        json_file = PAGES_DIR / "job" / "job.json"
        html_file = PAGES_DIR / "job" / "index.html"
        job_json = self.load_json_file(json_file)
        cont_html = self.get_content(html_file)
        html = ""
        for name, dates in job_json.items():
            started = dates['start']
            ended = dates['end'] or "now"
            msg = cont_html.format(name=name, started=started, ended=ended)
            #msg = json.dumps(job_json, sort_keys=True, indent=4)
            html += msg
        respond(self, html, "text/html")

    def load_json_file(self, fj):
        with fj.open("r") as j:
            return json.load(j)

    def handler_goodbye(self, method):
        self.visits_counter()
        time = datetime.now().hour
        parting = 'day' if time in range(9, 19) else 'night'
        msg = f'Good {parting}!'

        respond(self, msg, "text/plain")

    def visits_counter(self):
        stats = self.get_json(COUNTER)
        path = self.extract_path()
        #visits = stats.setdefault(datetime.now().strftime("%Y-%m-%d"), {})
        if path not in stats:
            stats[path] = 1
        stats[path] += 1
        self.save_data(stats)

    def save_data(self, stats):
        with COUNTER.open("w") as fp:
            json.dump(stats, fp)


    def get_json(self, file_inf):
        try:
            with file_inf.open("r", encoding="utf-8") as usf:
                return json.load(usf)
        except (json.JSONDecodeError, FileNotFoundError):
            return {}


    def handler_hello(self, method): #вытягиваем имя и возраст в хелло, сообщение
        self.visits_counter()
        args = self.build_query_args()
        name = self.build_name(args) #args.get("name", "dear")  #достать из словаря по ключу "имя"
        age = self.build_age(args) #args.get("age")    #дастать из словаря значение по ключу "возраст"

        msg = f'Hello, {name}!'

        if age:
            nowy = datetime.now().year
            year = nowy - int(age)
            msg += f'\n You was born at {year}!'

        respond(self, msg, "text/plain")

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
        #patha = self.path.split('?')[0]
        #pathb, *_qs = patha.split('#')[0]
        #if pathb[-1] == '/':
        #    path = pathb[:-1]
        #return path


with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("it works")
    httpd.serve_forever()
