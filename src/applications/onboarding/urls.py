from django.urls import path

import applications.onboarding.views.avatar_update
import applications.onboarding.views.profile
import applications.onboarding.views.profile_update
import applications.onboarding.views.sign_in
import applications.onboarding.views.sign_out
import applications.onboarding.views.sign_up
from applications.onboarding.apps import OnboardingConfig
from applications.onboarding import views

app_name = OnboardingConfig.label

urlpatterns = [
    path("profile/", applications.onboarding.views.profile.IndexView.as_view(), name="index"),
    path("profile-update/", applications.onboarding.views.profile_update.ProfileUpdateView.as_view(), name="profile-update"),
    path("avatar-update/", applications.onboarding.views.avatar_update.ChangeAvatarView.as_view(), name="avatar-update"),
    path("sign-in/", applications.onboarding.views.sign_in.SignInView.as_view(), name="sign-in"),
    path("sign-out/", applications.onboarding.views.sign_out.SignOutView.as_view(), name="sign-out"),
    path("sign-up/", applications.onboarding.views.sign_up.SignUpView.as_view(), name="sign-up"),
]
