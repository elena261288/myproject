from django.db import models


class Visit(models.Model):
    at = models.DateTimeField()
    cl = models.PositiveIntegerField()
    code = models.PositiveIntegerField()
    method = models.TextField()
    tm = models.FloatField()
    url = models.URLField()

