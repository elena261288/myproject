from django.views.generic import CreateView

from applications.job.models import Jobs
from applications.stats.utils import count_stats


@count_stats
class AddJobView(CreateView):
    model = Jobs
    #fields = ["company", "position", "started", "ended", "description"]
    fields = "__all__"


    def get_success_url(self):
        return self.object.get_absolute_path()
