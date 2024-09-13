from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from .models import Message

# Create your views here.

class MessageInboxView(ListView):
    http_method_names = ["get"]
    template_name = "messaging/inbox.html"
    model = Message
    context_object_name = "message"
 
    def get_queryset(self):
        return Message.objects.filter(msg_to=self.request.user).distinct('msg_from').order_by('date_sent')
    
    def get_object(self):
       return self.request.user

