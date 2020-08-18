from django.urls import reverse_lazy
from django.views.generic import RedirectView, DeleteView

from applications.job.models import Jobs
from applications.job.views.mixins import SingleObjectMixin


class DeleteJobView(DeleteView):
    model = Jobs
    #permanent = True
    #http_method_names = ["post"]
    success_url = reverse_lazy("job:all")

    #def get_redirect_url(self, *args, **kwargs):
     #   job = self.get_object()
     #   job.delete()

     #   return reverse_lazy("job:all")

