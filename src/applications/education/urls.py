from django.urls import path

from .apps import EducationConfig
from .views import EducationView

app_name = EducationConfig.label

urlpatterns = [
    path("", EducationView.as_view(), name="index")]
