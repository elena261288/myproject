import json

from django.conf import settings
from django.views.generic import TemplateView


class JobView(TemplateView):
    template_name = "job/index.html"

    #def get_context_data(self, **kwargs):
    #    ctx = super().get_context_data(**kwargs)
    #    json_file = "job/job.json"

    #    def load_json_file(fj):
    #        with fj.open("r") as j:
    #            return json.load(j)
    #    job_json = load_json_file(json_file)

    #    for name, dates in job_json.items():
    #        started = dates["start"]
    #        ended = dates["end"] or "now"

    #    ctx.update({
    #        "name": name

    #    })
    #    return ctx

