from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Parties

# Create your views here.

class Parties(ListView):
    html_method_names = ["get"]
    template_name = "comingsoon.html"
    models = Parties
    context_object_name = "events"
    queryset = Parties.objects.all().order_by('-id')[0:30]