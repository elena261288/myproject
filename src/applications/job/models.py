from django.db import models
from django.urls import reverse_lazy


class Jobs(models.Model):
    company = models.TextField(unique=True)
    position = models.TextField()
    started = models.DateField(null=True, blank=True)
    ended = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.company} ({self.pk})"

    def get_absolute_path(self):
        kwargs = {"pk": self.pk}
        return reverse_lazy("job:single", kwargs=kwargs)

