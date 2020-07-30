from django.urls import reverse_lazy
from django.views.generic import RedirectView

from applications.job.models import Jobs
from applications.job.views.mixins import SingleObjectMixin


class DeleteJobView(SingleObjectMixin, RedirectView):
    model = Jobs
    permanent = True
    http_method_names = ["post"]

    def get_redirect_url(self, *args, **kwargs):
        job = self.get_object()
        job.delete()

        return reverse_lazy("job:all")

