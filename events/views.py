from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Events
from .forms import EventCreateForm

# Create your views here.

class EventsList(ListView):
    html_method_names = ["get"]
    template_name = "events/list.html"
    models = Events
    context_object_name = "events"
    queryset = Events.objects.all().order_by('-id')[0:30]


class EventDetailView(DetailView):    
    html_method_names = ["get"]
    template_name = "events/detail.html"
    models = Events,
    context_object_name = "event"


class PageAddEventView(LoginRequiredMixin, CreateView):
    models = Events
    form_class = EventCreateForm
    template_name = "events/add_event.html"
    queryset = Events.objects.all()
    success_message = "Your event was added successfully"
    success_url = "/"

    def form_valid(self, form):
        form.instance.location_id = self.kwargs.get('pk')        
        form.instance.organiser = self.request.user
        return super(PageAddEventView, self).form_valid(form)

    def get_object(self):
       return self.request.user