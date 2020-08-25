from django.views.generic import ListView

from applications.blog.models import Blogs
from applications.stats.utils import count_stats


@count_stats
class AllBlogView(ListView):
    template_name = "blog/all.html"
    model = Blogs
