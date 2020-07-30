from datetime import datetime

from django.views.generic import TemplateView

from applications.stats.utils import count_stats


@count_stats
class GoodbyeView(TemplateView):
    template_name = "goodbye/index.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        time = datetime.now().hour
        parting = "day" if time in range(9, 19) else "night"

        ctx.update({
            "tod": parting
        })
        return ctx


