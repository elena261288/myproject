from django import forms
from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from applications.blog.models import Blogs


class BlogsAdminForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = "__all__"
        widgets ={
            "theme": forms.TextInput(),
        }


@admin.register(Blogs)
class BlogsAdminModel(ModelAdmin):
    form = BlogsAdminForm
