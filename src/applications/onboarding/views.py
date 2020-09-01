from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, DetailView

from applications.onboarding.models import Profile
from applications.stats.utils import count_stats


@count_stats
class IndexView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "onboarding/index.html"

    def get_object(self, queryset=None):
        if self.request.user.is_anonymous:
            return None

        if not queryset:
            queryset = self.model.objects.all()

        queryset = queryset.filter(user=self.request.user)

        return queryset.first()


class SignInView(LoginView):
    template_name = "onboarding/sign_in.html"


class SignOutView(LogoutView):
    template_name = "onboarding/sign_out.html"
