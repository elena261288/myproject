from dataclasses import dataclass
from datetime import date
from typing import Optional

from project.models import Model


@dataclass
class Jobs(Model):
    company: Optional[str] = None
    position: Optional[str] = None
    started: Optional[date] = None
    ended: Optional[date] = None
    description: Optional[str] = None

    __json_file__ = "job.json"
