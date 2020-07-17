from django.contrib import admin
from django.urls import path

from project.views import (
    handle_goodbye,
    handle_education,
    handle_index,
    handle_skills,
    handle_job,
    handle_hello, handle_theme,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", handle_index),
    path("hello/", handle_hello),
    path("goodbye/", handle_goodbye),
    path("education/", handle_education),
    path("skills/", handle_skills),
    path("job/", handle_job),
    path("theme/", handle_theme),
]
