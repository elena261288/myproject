from django.urls import reverse_lazy
from django.views.generic import UpdateView

from applications.onboarding.forms import AvatarForm
from applications.onboarding.mixins import CurrentUserMixin
from applications.stats.utils import count_stats


@count_stats
class ChangeAvatarView(CurrentUserMixin, UpdateView):
    http_method_names = ["post"]
    form_class = AvatarForm
    success_url = reverse_lazy("onboarding:index")

    def get_object(self, queryset=None):
        return self.get_current_avatar()
