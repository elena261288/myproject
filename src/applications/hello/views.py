from datetime import datetime

from django import forms
from django.shortcuts import render
from django.views.generic import FormView

from applications.stats.utils import count_stats
from utility.util import load_user_session, build_query_args, build_name, build_age


class HelloForm(forms.Form):
    name = forms.CharField(max_length=200, required=True)
    age = forms.IntegerField()


@count_stats
class HelloView(FormView):
    template_name = "hello/index.html"
    success_url = "/hello/"
    form_class = HelloForm

    def get_initial(self):
        name, age = self.build_name_age()
        return {
            "name": name or "",
            "age": age or None
        }

    def get_context_data(self, **kwargs):
        parent_ctx = super().get_context_data(**kwargs)

        name, age = self.build_name_age()
        born = None
        if age:
            year = datetime.now().year
            born = year - int(age)

        local_ctx = {
            "name": name,
            "year": born
          }
        local_ctx.update(parent_ctx)

        return local_ctx

    def form_valid(self, form):
        self.request.session["name"] = form.cleaned_data["name"]
        self.request.session["age"] = form.cleaned_data["age"]
        return super().form_valid(form)

    def build_name_age(self):
        sessions = load_user_session(self.request) or build_query_args(self.request.path)
        name = build_name(sessions)
        age = build_age(sessions)
        return name, age






