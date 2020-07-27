from dataclasses import asdict

from django import forms
from django.views.generic import FormView, RedirectView

from applications.job.models import Jobs


class JobForm(forms.Form):
    company = forms.CharField(max_length=200)
    position = forms.CharField(max_length=200)
    started = forms.DateField()
    ended = forms.DateField(required=False)
    description = forms.CharField(required=False, widget=forms.Textarea)


class AllJobView(FormView):
    template_name = "job/all.html"
    form_class = JobForm
    success_url = "/job/"

    def form_valid(self, form):
        job = Jobs(**form.cleaned_data)
        job.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["object_list"] = Jobs.all()
        return ctx


class SingleObjectMixin:
    model = None

    def get_object_id(self):
        return self.kwargs["job_id"]

    def get_object(self):
        object_id = self.get_object_id()
        return self.model.one(object_id)


class SingleJobView(SingleObjectMixin, FormView):
    model = Jobs
    template_name = "job/single.html"
    form_class = JobForm
    success_url = "/job/"

    def get_initial(self):
        job =self.get_object()
        dct = asdict(job)
        try:
            del dct["pk"]
        except KeyError:
            pass
        return dct

    def get_success_url(self):
        job_id = self.get_object_id()
        return f"/job/{job_id}/"

    def form_valid(self, form):
        job = self.get_object()
        for key, value in form.cleaned_data.items():
            setattr(job, key, value)
        job.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        job = self.get_object()
        ctx["object"] = job
        return ctx


class DeleteJobView(SingleObjectMixin, RedirectView):
    model = Jobs
    permanent = True
    http_method_names = ["post"]

    def get_redirect_url(self, *args, **kwargs):
        job = self.get_object()
        job.delete()

        return "/job/"