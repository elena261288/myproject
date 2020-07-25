from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class EducationView(TemplateView):
    template_name = "education/index.html"

