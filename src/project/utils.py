import json
import os
from urllib.parse import parse_qs


def get_content(fp):
    with fp.open("r", encoding="utf-8") as src:
        con = src.read()
        return con


def load_json_file(fj):
    with fj.open("r") as j:
        return json.load(j)


def load_user_session(request, file):
    session_id = get_session_id(request)
    if not session_id:
        return {}
    session = get_json(file)
    return session.get(session_id, {})


def get_session_id(request):
    cookie = request.headers.get("Cookie")
    if not cookie:
        return {}
    cookie = cookie.split(";")[0]

    return cookie


def save_user_session(request, session, fj):
    session_id = get_session_id(request) or os.urandom(16).hex()
    sessions = get_json(fj)
    sessions[session_id] = session
    save_id(fj, sessions)

    return session_id


def save_id(file, id):
    with file.open("w") as fp:
        json.dump(id, fp)





def get_json(file_inf):
    try:
        with file_inf.open("r", encoding="utf-8") as usf:
            return json.load(usf)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}


def build_query_args(path):  # разбиваем qs на словарь qs
    _path, *qs = path.split("?")
    args = {}

    if len(qs) != 1:
        return args

    qs = qs[0]  # преобразовали из списка в строку
    qs = parse_qs(qs)

    for key, value in qs.items():
        if not value:
            continue

        args[key] = value[0]
    return args


def build_name(query_args):
    return query_args.get("name", "friend")


def build_age(query_args):
    return query_args.get("age")

def get_form(request):
    #content_length = int(request.headers["Content-Length"])
    #data = request.rfile.read(content_length)
    #payload = data.decode()
    #qs = parse_qs(payload)
    result = {}
    for key, values in request.POST.items():
        if not values:
            continue

        result[key] = values
    return result
