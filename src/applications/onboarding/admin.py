from django.contrib.admin import ModelAdmin

from applications.onboarding.models import Profile
from django.contrib import admin


@admin.register(Profile)
class ProfileAdminModel(ModelAdmin):
    pass


