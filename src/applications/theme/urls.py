from django.urls import path

from .apps import ThemeConfig
from .views import SwitchThemeView

app_name = ThemeConfig.label

urlpatterns = [
    #path("", views.ThemeView.as_view(), name="index"),
    path("switcher/", SwitchThemeView.as_view(), name="switch")]




