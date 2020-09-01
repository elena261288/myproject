from django.urls import path

from applications.onboarding.apps import OnboardingConfig
from applications.onboarding import views

app_name = OnboardingConfig.label

urlpatterns = [
    path("profile/", views.IndexView.as_view(), name="index"),
    path("profile-update/", views.ProfileUpdateView.as_view(), name="profile-update"),
    path("sign-in/", views.SignInView.as_view(), name="sign-in"),
    path("sign-out/", views.SignOutView.as_view(), name="sign-out"),
    path("sign-up/", views.SignUpView.as_view(), name="sign-up"),
]
