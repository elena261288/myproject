from django.shortcuts import render


#def IndexView(request):
#    return render(request, "target/index.html")
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "target/index.html"