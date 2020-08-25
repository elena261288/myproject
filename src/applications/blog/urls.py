from django.urls import path

from .apps import BlogConfig
from .views import AddBlogView
from .views.all import AllBlogView
from .views.delete import DeleteBlogView
from .views.single import SingleBlogView

app_name = BlogConfig.label

urlpatterns = [
    path("", AllBlogView.as_view(), name="all"),
    path("add/", AddBlogView.as_view(), name="add"),
    path("b/<str:pk>/", SingleBlogView.as_view(), name="single"),
    path("b/<str:pk>/delete/", DeleteBlogView.as_view(), name="delete")
]


