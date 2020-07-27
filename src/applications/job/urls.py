from django.urls import path

from .apps import JobConfig
from .views import AllJobView, SingleJobView

app_name = JobConfig.label

urlpatterns = [
    path("", AllJobView.as_view(), name="all_job"),
    path("<str:job_id>/", SingleJobView.as_view(), name="single_job"),
]


