import logging
from datetime import datetime

from django.conf import settings
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods

from project.utils import load_user_session, build_query_args, build_name, build_age, get_content, load_json_file, \
    get_form, save_user_session, get_theme, switch_theme

SESSION = settings.PAGES_DIR / "hello" / "session.json"


def handle_index(request):
    html = settings.REPO_DIR / "index.html"
    content = get_content(html)
    return HttpResponse(content)


@require_http_methods(["GET", "POST"])
def handle_hello(request: HttpRequest):
    logging.debug(f"request = {request}")

    switcher = {
        "GET": handle_hello_get,
        "POST": handle_hello_post
    }

    handler = switcher[request.method]
    return handler(request)


def handle_hello_get(request):
    sessions = load_user_session(request, SESSION) or build_query_args(request.path)
    name = build_name(sessions)
    age = build_age(sessions)
    born = None
    if age:
        year = datetime.now().year
        born = year - int(age)

    html_file = settings.PAGES_DIR / "hello" / "index.html"
    cont_html = get_content(html_file).format(name=name, year=born)
    return HttpResponse(cont_html, "text/html")


def handle_hello_post(request):
    form = get_form(request)
    session = load_user_session(request, SESSION)
    session.update(form)
    session_id = save_user_session(request, session, SESSION)
    response = HttpResponseRedirect("/hello")
    response.set_cookie("SESSION_ID" or " SESSION_ID", session_id)
    return response


def handle_goodbye(request):
    time = datetime.now().hour
    parting = "day" if time in range(9, 19) else "night"
    msg = f"Good {parting}!"
    return HttpResponse(msg)


def handle_education(request):
    html_doc = settings.PAGES_DIR / "education" / "index.html"
    content = get_content(html_doc)
    return HttpResponse(content)


def handle_skills(request):
    html = settings.PAGES_DIR / "skills" / "index.html"
    content = get_content(html)
    return HttpResponse(content)


def handle_job(request):
    json_file = settings.PAGES_DIR / "job" / "job.json"
    html_file = settings.PAGES_DIR / "job" / "index.html"
    job_json = load_json_file(json_file)
    cont_html = get_content(html_file)
    html = ""
    for name, dates in job_json.items():
        started = dates["start"]
        ended = dates["end"] or "now"
        msg = cont_html.format(name=name, started=started, ended=ended)
        html += msg
    return HttpResponse(html)


@require_http_methods(["GET", "POST"])
def handle_theme(request):
    def handle_theme_get():
        theme = get_theme(request)

        con_html = get_content(settings.PAGES_DIR / "theme" / "index.html")
        style_html = get_content(settings.PAGES_DIR / "theme" / "theme.html")

        kw = {
            "style": style_html,
            "class": theme
        }
        html = con_html.format(**kw)
        return HttpResponse(html)

    def handle_theme_post():
        switch_theme(request)
        return redirect("/theme/")

    switcher = {
        "GET": handle_theme_get,
        "POST": handle_theme_post,
    }

    handler = switcher[request.method]
    return handler()
