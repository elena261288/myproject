from django.views.generic import TemplateView

from applications.stats.utils import count_stats


@count_stats
class EducationView(TemplateView):
    template_name = "education/index.html"

