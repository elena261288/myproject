from django.urls import path

from project.views import handler_goodbye, handler_education, handler_index, handler_skills, handler_job

urlpatterns = [
    path('admin/', handler_index),
    path('goodbye/', handler_goodbye),
    path('education/', handler_education),
    path('skills/', handler_skills),
    path('job/', handler_job)
]

