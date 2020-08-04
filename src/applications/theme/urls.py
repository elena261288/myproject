from django.urls import path

from .apps import ThemeConfig
from .views import SwitchThemeView


app_name = ThemeConfig.label

urlpatterns = [
    path("", SwitchThemeView.as_view(), name="switcher")

    ]




