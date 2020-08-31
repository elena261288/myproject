from django.urls import path

from applications.onboarding.apps import OnboardingConfig

from applications.onboarding.views import IndexView

app_name = OnboardingConfig.label

urlpatterns = [
    path("", IndexView.as_view(), name="index")]