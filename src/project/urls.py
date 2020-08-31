from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("applications.target.urls")),
    path("hello/", include("applications.hello.urls")),
    path("goodbye/", include("applications.goodbye.urls")),
    path("education/", include("applications.education.urls")),
    path("skills/", include("applications.skills.urls")),
    path("job/", include("applications.job.urls")),
    path("theme/", include("applications.theme.urls")),
    path("stats/", include("applications.stats.urls")),
    path("blog/", include("applications.blog.urls")),
    path("user/", include("applications.onboarding.urls")),
]

