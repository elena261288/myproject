from django.contrib.admin import ModelAdmin

from applications.onboarding.models import Profile, Avatar
from django.contrib import admin


@admin.register(Profile)
class ProfileAdminModel(ModelAdmin):
    pass


@admin.register(Avatar)
class AvatarAdminModel(ModelAdmin):
    pass


