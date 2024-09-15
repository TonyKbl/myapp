from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from itertools import chain
from operator import attrgetter

from .models import Message

# Create your views here.

class MessageInboxView(LoginRequiredMixin, ListView):
    
    http_method_names = ["get"]
    template_name = "messaging/inbox.html"
    model = Message
    context_object_name = "message"

 
    def get_queryset(self):
        return Message.objects.filter(msg_to=self.request.user).distinct('msg_from')

    
    def get_object(self):
       return self.request.user


class MessageView(LoginRequiredMixin, ListView):
    
    http_method_names = ["get"]
    template_name = "messaging/message.html"
    model = Message
    context_object_name = "message_list"

 
    def get_queryset(self):
        qs1 = Message.objects.filter(Q(msg_to=self.request.user) & Q(msg_from=self.kwargs['pk']))
        qs2 = Message.objects.filter(Q(msg_from=self.request.user) & Q(msg_to=self.kwargs['pk']))
        queryset = sorted(chain(qs1,qs2),key=attrgetter('date_sent', 'time_sent'),reverse=True)[:25]
        return queryset
        # return Message.objects.filter(Q(msg_to=self.request.user) | Q(msg_from=self.request.user))

            # return PagePost.objects.filter(id=self.kwargs['pk'])
    #  def get_queryset(self):
        
    #     followed_users = self.request.user.following.all()      
    #     qs1 = Post.objects.filter(Q(author__in=followed_users.values('following'))) #your first qs

    #     followed_pages = self.request.user.page_following.all()
    #     qs2 = PagePost.objects.filter(Q(name__in=followed_pages.values('following')))  #your second qs
        
    #     queryset = sorted(chain(qs1,qs2),key=attrgetter('date'),reverse=True)[:25]
    #     return queryset
    

    def get_object(self):
       return self.request.user