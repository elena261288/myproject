from django.contrib.auth import get_user_model
from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    birth_date = models.DateField(null=True, blank=True)
    display_name = models.TextField(null=True, blank=True)

    def __str__(self):
        msg = f"{self.display_name} ({self.user.username})"
        return msg


class Avatar(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, primary_key=True)
    original = models.FileField(storage=S3Boto3Storage())
