from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from project.views import (
    handle_index,
    handle_skills,
    handle_job,
    handle_hello, handle_theme, #handle_counter,
)
from applications.education.views import handle_education
from applications.goodbye.views import handle_goodbye

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("applications.target.urls")),
    #path("", handle_index),
    path("hello/", handle_hello),
    path("goodbye/", include("applications.goodbye.urls")),
    path("education/", include("applications.education.urls")),
    path("skills/", handle_skills),
    path("job/", handle_job),
    path("theme/", handle_theme),
    #path("counter/", handle_counter),
]
