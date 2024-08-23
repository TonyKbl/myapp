from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Events

# Create your views here.

class Events(ListView):
    html_method_names = ["get"]
    template_name = "comingsoon.html"
    models = Events
    context_object_name = "events"
    queryset = Events.objects.all().order_by('-id')[0:30]