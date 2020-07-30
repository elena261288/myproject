from django.urls import reverse_lazy
from django.views.generic import FormView

from applications.job.forms import JobForm
from applications.job.models import Jobs
from applications.job.views.mixins import SingleObjectMixin

from applications.stats.utils import count_stats


@count_stats
class SingleJobView(SingleObjectMixin, FormView):
    model = Jobs
    template_name = "job/single.html"
    form_class = JobForm

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        job = self.get_object()
        ctx["object"] = job
        return ctx

    def get_initial(self):
        dct = self.get_object_dct()
        self.shadow_pk(dct)
        return dct

    def get_success_url(self):
        job_id = self.get_object_id()
        kwargs = {"pk": job_id}
        url = reverse_lazy("job:single", kwargs=kwargs)
        return url

    def form_valid(self, form):
        job = self.get_object()
        self.update_object(job, form)
        job.save()
        return super().form_valid(form)



