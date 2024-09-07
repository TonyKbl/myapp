from django.db.models.base import Model as Model
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from pages.models import Page
from .models import Event
from .forms import EventCreateForm

# Create your views here.

class EventsList(ListView):
    html_method_names = ["get"]
    template_name = "events/list.html"
    models = Event
    context_object_name = "events"
    queryset = Event.objects.all().order_by('-id')[0:30]


class PageEventsList(ListView):
    # html_method_names = ["get"]
    # template_name = "events/list.html"
    # models = Events
    # context_object_name = "events"
    # queryset = Events.objects.all().order_by('-id')[0:30]
    http_method_names = ["get"]
    template_name = "events/list.html"
    model = Page
    context_object_name = "page"

    def get_context_data(self, *args, **kwargs):
        context = super(PageEventsList, self).get_context_data(*args, **kwargs)
        context['events'] = Event.objects.filter(location__slug=self.kwargs['slug'])
        return context


class EventDetailView(DetailView):    
    html_method_names = ["get"]
    template_name = "events/detail.html"
    models = Event,
    context_object_name = "event"

    def get_queryset(self, **kwargs):
        return Event.objects.filter(id=self.kwargs['pk'])


class PageAddEventView(LoginRequiredMixin, CreateView):
    models = Event
    form_class = EventCreateForm
    template_name = "events/add_event.html"
    queryset = Event.objects.all()
    success_message = "Your event was added successfully"
    success_url = "/"

    def form_valid(self, form):
        form.instance.location_id = self.kwargs.get('pk')        
        form.instance.organiser = self.request.user
        return super(PageAddEventView, self).form_valid(form)

    def get_object(self):
       return self.request.user