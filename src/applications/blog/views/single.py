from typing import Dict

from django.urls import reverse_lazy
from django.views.generic import FormView

from applications.blog.forms import BlogForm
from applications.blog.models import Blogs
from applications.blog.views.mixins import SingleObjectMixin

from applications.stats.utils import count_stats


@count_stats
class SingleBlogView(SingleObjectMixin, FormView):
    model = Blogs
    template_name = "blog/single.html"
    form_class = BlogForm

    def get_object_dct(self) -> Dict:
        obj = self.get_object()
        dct = {"theme": obj.theme,
               "description": obj.description,
               "content": obj.content,
        }
        return dct

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        blog = self.get_object()
        ctx["object"] = blog
        return ctx

    def get_initial(self):
        dct = self.get_object_dct()
        self.shadow_pk(dct)
        return dct

    def get_success_url(self):
        blog_id = self.get_object_id()
        kwargs = {"pk": blog_id}
        url = reverse_lazy("blog:single", kwargs=kwargs)
        return url

    def form_valid(self, form):
        blog = self.get_object()
        self.update_object(blog, form)
        blog.save()
        return super().form_valid(form)



