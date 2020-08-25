from django.urls import reverse_lazy
from django.views.generic import DeleteView

from applications.blog.models import Blogs


class DeleteBlogView(DeleteView):
    model = Blogs
    success_url = reverse_lazy("blog:all")

