from django.urls import path

from .apps import SkillsConfig
from .views import SkillsView

app_name = SkillsConfig.label

urlpatterns = [
    path("", SkillsView.as_view(), name="index")]



