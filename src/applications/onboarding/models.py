from django.contrib.auth import get_user_model
from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage

User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    birth_date = models.DateField(null=True, blank=True)
    display_name = models.TextField(null=True, blank=True)


class Avatar(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    original = models.FileField(storage=S3Boto3Storage())
