from django.urls import reverse_lazy
from django.views.generic import ListView

from applications.job.models import Jobs
from applications.stats.utils import count_stats


@count_stats
class AllJobView(ListView):
    template_name = "job/all.html"
    #form_class = JobForm
    #success_url = reverse_lazy("job:all")
    model = Jobs
    #queryset = Jobs.objects.filter(visible=True)

    #def form_valid(self, form):
    #    job = Jobs(**form.cleaned_data)
    #    job.save()
    #    return super().form_valid(form)

    #def get_context_data(self, **kwargs):
    #    ctx = super().get_context_data(**kwargs)
    #    ctx["object_list"] = Jobs.objects.all()
    #    return ctx

