from datetime import datetime

from django.db import models
from django.urls import reverse_lazy


class Blogs(models.Model):
    created = models.DateTimeField(default=datetime.utcnow, editable=False)
    theme = models.TextField()
    description = models.TextField(null=True, blank=True)
    content = models.TextField()

    def __str__(self) -> str:
        return f"{self.created} ({self.pk})"

    def get_absolute_path(self):
        kwargs = {"pk": self.pk}
        return reverse_lazy("blog:single", kwargs=kwargs)

