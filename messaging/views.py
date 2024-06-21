from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Messages

# Create your views here.

class Messages(ListView):
    html_method_names = ["get"]
    template_name = "messages.html"
    models = Messages
    context_object_name = "messages"
    queryset = Messages.objects.all().order_by('-id')[0:30]