from profile import Profile

from django.views.generic import TemplateView, DetailView

from applications.stats.utils import count_stats


@count_stats
class IndexView(DetailView):
    model = Profile
    template_name = "onboarding/index.html"

    def get_object(self, queryset=None):
        if self.request.user.is_anonimus:
            return None
        if not queryset:
            queryset = self.model.object.all()

        queryset = queryset.filter(user=self.request.user)

        return queryset.first()