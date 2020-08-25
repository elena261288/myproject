from django import forms
from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from applications.job.models import Jobs


class JobsAdminForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = "__all__"
        widgets ={
            "company": forms.TextInput(),
        }


@admin.register(Jobs)
class JobsAdminModel(ModelAdmin):
    form = JobsAdminForm
