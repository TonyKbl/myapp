from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Message

# Create your views here.

class MessageInboxView(LoginRequiredMixin, ListView):
    # html_method_names = ["get"]
    # template_name = "messaging/messages.html"
    # models = Message
    # context_object_name = "message"
    # queryset = Message.objects.all().order_by('-id')



    http_method_names = ["get"]
    template_name = "messaging/inbox.html"
    model = Message
    context_object_name = "message"

 
    def get_queryset(self):
        return Message.objects.filter(msg_to=self.request.user).distinct('msg_from')
        # message = Message.objects.raw('''SELECT * FROM messaging_message WHERE msg_to_id = '4' ORDER_BY date_sent''')
        # print(message)
        # return message

    
    def get_object(self):
       return self.request.user

    # target_user = id
    # context = {'target_user':target_user}

    # def get_context_data(self, *args, **kwargs):
    #     context = super(MessageListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     # context['message'] = Message.objects.filter(msg_from__username=self.kwargs['slug']).order_by('-date_sent')
    #     context['message'] = Message.objects.filter(msg_from__username=context.user.username).order_by('-date_sent')
    #     return context