from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django import forms
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, FormView
from django.views.generic.edit import FormMixin, UpdateView

from applications.onboarding.models import Profile
from applications.stats.utils import count_stats

User = get_user_model()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class CurrentUserMixin:
    def get_object(self, *_args, **_kwargs):
        if self.request.user.is_anonymous:
            return None

        queryset = self.model.objects.filter(user=self.request.user)

        return queryset.first()


@count_stats
class IndexView(CurrentUserMixin, FormMixin, LoginRequiredMixin, DetailView):
    form_class = ProfileForm
    model = Profile
    template_name = "onboarding/index.html"

    def get_initial(self):
        model_attrs = {Profile.birth_date, Profile.display_name}
        model_fields = {attr.field.name for attr in model_attrs}
        initial = {field: getattr(self.object, field) for field in model_fields}
        return initial

@count_stats
class ProfileUpdateView(CurrentUserMixin, UpdateView):
    http_method_names = ["post"]
    form_class = ProfileForm
    model = Profile
    success_url = reverse_lazy("onboarding:index")

@count_stats
class SignInView(LoginView):
    template_name = "onboarding/sign_in.html"

@count_stats
class SignOutView(LogoutView):
    template_name = "onboarding/sign_out.html"


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = (
            "email",
            "password1",
            "password2",
            "username",
        )

@count_stats
class SignUpView(FormView):
    form_class = SignUpForm
    success_url = reverse_lazy("onboarding:index")
    template_name = "onboarding/sign-up.html"

    def form_valid(self, form):
        form.save()

        username = form.cleaned_data["username"]
        password = form.cleaned_data["password1"]

        user = authenticate(self.request, username=username, password=password)
        login(self.request, user)

        profile = Profile(user=user)
        profile.save()

        return super().form_valid(form)
