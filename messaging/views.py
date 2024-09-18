from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from itertools import chain
from operator import attrgetter

from .models import Message
from .forms import MessageSendForm
from profiles.models import Profile

# Create your views here.

class MessageInboxView(LoginRequiredMixin, ListView):
    
    http_method_names = ["get"]
    template_name = "messaging/inbox.html"
    model = Message
    context_object_name = "message"

 
    def get_queryset(self):
        return Message.objects.filter(msg_to=self.request.user).distinct('msg_from').order_by()

    
    def get_object(self):
       return self.request.user


class MessageView(LoginRequiredMixin, ListView):
    
    http_method_names = ["get"]
    template_name = "messaging/message.html"
    model = Message, User, Profile
    context_object_name = "message_list"

 
    def get_queryset(self):
        qs1 = Message.objects.filter(Q(msg_to=self.request.user) & Q(msg_from=self.kwargs['pk']))
        qs2 = Message.objects.filter(Q(msg_from=self.request.user) & Q(msg_to=self.kwargs['pk']))
        queryset = sorted(chain(qs1,qs2),key=attrgetter('date_sent', 'time_sent'),reverse=True)[:25]
        return queryset
    
    def get_context_data(self, *args, **kwargs):
        context = super(MessageView, self).get_context_data(*args, **kwargs)
        context['profile'] = Profile.objects.filter(user__id=self.kwargs['pk']).values()
        return context
    
    def get_object(self, queryset=None):
        obj = Profile.objects.get(id=self.kwargs.get('pk'))
        return obj

    def get_object(self):
       return self.request.user
    

class SendMessageView(LoginRequiredMixin, CreateView):
    template_name = "messaging/send.html"
    model = Message    
    form_class = MessageSendForm
    context_object_name = "message_send"
    queryset = Message.objects.all()
    success_url = '/'

    def form_valid(self, form):
        form.instance.msg_to_id = self.kwargs.get('pk')        
        form.instance.msg_from = self.request.user
        return super(SendMessageView, self).form_valid(form)