from applications.stats import views
from django.urls import path

from .apps import StatsConfig

app_name = StatsConfig.label

urlpatterns = [
    path("", views.StatsView.as_view(), name="index"),
    path("reset/", views.ResetView.as_view(), name="reset")]




