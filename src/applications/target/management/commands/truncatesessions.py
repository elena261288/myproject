from django.core.management.base import BaseCommand
from django.contrib.sessions.models import Session


class Command(BaseCommand):
    help = 'Deletes all sessions'

    def handle(self, *args, **options):
        Session.objects.all().delete()


