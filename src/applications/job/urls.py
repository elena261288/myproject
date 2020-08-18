from django.urls import path

from .apps import JobConfig
from .views import AddJobView
from .views.all import AllJobView
from .views.delete import DeleteJobView
from .views.single import SingleJobView

app_name = JobConfig.label

urlpatterns = [
    path("", AllJobView.as_view(), name="all"),
    path("add/", AddJobView.as_view(), name="add"),
    path("j/<str:pk>/", SingleJobView.as_view(), name="single"),
    path("j/<str:pk>/delete/", DeleteJobView.as_view(), name="delete")
]


