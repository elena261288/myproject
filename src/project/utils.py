import json
from urllib.parse import parse_qs

from django.urls import path
from http.server import SimpleHTTPRequestHandler

from httpie.output.formatters import headers

from project.constants import SESSION


def get_content(request, fp):
    with fp.open("r", encoding="utf-8") as src:
        con = src.read()
        return con


def load_json_file(request, fj):
    with fj.open("r") as j:
        return json.load(j)


def load_user_session(request):
    session_id = get_session_id()
    if not session_id:
        return {}
    session = get_json(SESSION)
    return session.get(session_id, {})


def get_session_id(request):
    cookie = headers.get("Cookie")
    if not cookie:
        return {}
    cookie = cookie.split(";")[0]
    return cookie


def get_json(request, file_inf):
    try:
        with file_inf.open("r", encoding="utf-8") as usf:
            return json.load(usf)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}


def build_query_args(request):  # разбиваем qs на словарь qs
    _path, *qs = path.split("?")
    args = {}

    if len(qs) != 1:
        return args

    qs = qs[0]  # преобразовали из списка в строку
    qs = parse_qs(qs)

    for key, value in qs.items():  # для каждого картежа "ключ-знач" выполнить...
        if not value:
            continue

        args[key] = value[0]
    return args


def build_name(request, query_args):
    return query_args.get("name", "friend")


def build_age(request, query_args):
    return query_args.get("age")
