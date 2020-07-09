from datetime import datetime

from django.http import HttpResponse

from project.constants import PAGES_DIR, MYPROJECT_DIR
from project.utils import get_content, load_json_file


def handler_index(request):
    html = MYPROJECT_DIR / "index.html"
    content = get_content(request, html)
    return HttpResponse(content, html)


def handler_goodbye(request):
    time = datetime.now().hour
    parting = "day" if time in range(9, 19) else "night"
    msg = f"Good {parting}!"
    return HttpResponse(msg)


def handler_education(request):
    html = PAGES_DIR / "education" / "index.html"
    content = get_content(request, html)
    return HttpResponse(content, html)


def handler_skills(request):
    html = PAGES_DIR / "skills" / "index.html"
    content = get_content(request, html)
    return HttpResponse(content, html)


def handler_job(request):
    json_file = PAGES_DIR / "job" / "job.json"
    html_file = PAGES_DIR / "job" / "index.html"
    job_json = load_json_file(request, json_file)
    cont_html = get_content(request, html_file)
    html = ""
    for name, dates in job_json.items():
        started = dates["start"]
        ended = dates["end"] or "now"
        msg = cont_html.format(name=name, started=started, ended=ended)
        html += msg
    return HttpResponse(request, html)

