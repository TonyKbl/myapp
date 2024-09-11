from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Message

# Create your views here.

class Messages(ListView):
    html_method_names = ["get"]
    template_name = "messages.html"
    models = Message
    context_object_name = "messages"
    queryset = Message.objects.all().order_by('-id')[0:30]