from django import forms


class JobForm(forms.Form):
    company = forms.CharField(max_length=200)
    position = forms.CharField(max_length=200)
    started = forms.DateField()
    ended = forms.DateField(required=False)
    description = forms.CharField(required=False, widget=forms.Textarea)
