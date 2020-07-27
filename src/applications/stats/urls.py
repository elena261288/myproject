from django.urls import path

from .apps import StatsConfig
from .views import StatsView

app_name = StatsConfig.label

urlpatterns = [
    path("", StatsView.as_view(), name="index")]



