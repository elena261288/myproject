from django.db import models


class Jobs(models.Model):
    company = models.TextField(unique=True)
    position = models.TextField()
    started = models.DateField(null=True, blank=True)
    ended = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

