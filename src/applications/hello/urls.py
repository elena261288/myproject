from django.urls import path

from .apps import HelloConfig
from .views import HelloView

app_name = HelloConfig.label

urlpatterns = [
    path("", HelloView.as_view(), name="index")]

