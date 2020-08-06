from django.views.generic import TemplateView

from applications.stats.utils import count_stats


@count_stats
class SkillsView(TemplateView):
    template_name = "skills/index.html"
