from django.views.generic import TemplateView


class SkillsView(TemplateView):
    template_name = "skills/index.html"
