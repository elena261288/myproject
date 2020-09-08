from django.contrib.auth.views import LogoutView

from applications.stats.utils import count_stats


@count_stats
class SignOutView(LogoutView):
    template_name = "onboarding/sign_out.html"