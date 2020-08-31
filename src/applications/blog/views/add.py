from django.views.generic import CreateView

from applications.blog.models import Blogs
from applications.stats.utils import count_stats


@count_stats
class AddBlogView(CreateView):
    model = Blogs
    fields = "__all__"

    def get_success_url(self):
        return self.object.get_absolute_path()
