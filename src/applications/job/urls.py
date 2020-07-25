from django.urls import path

from .apps import JobConfig
from .views import JobView

app_name = JobConfig.label

urlpatterns = [
    path("", JobView.as_view(), name="index")]

