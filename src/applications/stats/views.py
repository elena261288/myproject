from django.urls import reverse_lazy
from django.views.generic import TemplateView, RedirectView, ListView

from applications.stats.models import Visit
from applications.stats.utils import count_stats


@count_stats
class StatsView(ListView):
    template_name = "stats/index.html"
    #model = Visit
    queryset = Visit.objects.all()


    #def get_context_data(self, **kwargs):
    #    ctx = super().get_context_data(**kwargs)

     #   ctx["object_list"] = sorted(Visit.objects.all(), key=lambda v: -v.at.timestamp())

     #   return ctx


class ResetView(RedirectView):
    http_method_names = ["post"]

    def get_redirect_url(self, *args, **kwargs):
        Visit.objects.all().delete()
        return reverse_lazy("stats:index")
