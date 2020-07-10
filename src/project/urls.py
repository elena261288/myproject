from django.contrib import admin
from django.urls import path

from project.views import (
    handler_goodbye,
    handler_education,
    handler_index,
    handler_skills,
    handler_job,
    hello_GEThandler,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", handler_index),
    #path("hello/", hello_GEThandler),
    path("goodbye/", handler_goodbye),
    path("education/", handler_education),
    path("skills/", handler_skills),
    path("job/", handler_job),
]
