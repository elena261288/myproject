from django import forms


class BlogForm(forms.Form):
    theme = forms.CharField(max_length=140)
    description = forms.CharField(max_length=140)
    content = forms.CharField()
