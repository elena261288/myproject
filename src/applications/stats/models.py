from typing import Optional, NamedTuple

from django.db import models


class LimitsT(NamedTuple):
    min: float
    max: float
    avg: float


class IntervalT(NamedTuple):
    min05: LimitsT
    min10: LimitsT
    h01: LimitsT
    h24: LimitsT


class DashboardT(NamedTuple):
    Latency: IntervalT
    Traffic: IntervalT


class Visit(models.Model):
    at = models.DateTimeField(null=True, blank=True)
    cl = models.PositiveIntegerField(null=True, blank=True)
    code = models.PositiveIntegerField(null=True, blank=True)
    method = models.TextField(null=True, blank=True)
    tm = models.FloatField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ['-at']
