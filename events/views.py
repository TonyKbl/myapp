from django.db.models.base import Model as Model
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from pages.models import Page, PageHost
from .models import Event, EventDate
from .forms import EventCreateForm, EventAddDatesForm

# Create your views here.

class EventsList(ListView):
    html_method_names = ["get"]
    template_name = "events/date_list.html"
    models = EventDate
    context_object_name = "events"
    queryset = EventDate.objects.all().order_by('date')[0:30]


class PageEventsList(ListView):
    # html_method_names = ["get"]
    # template_name = "events/list.html"
    # models = Events
    # context_object_name = "events"
    # queryset = Events.objects.all().order_by('-id')[0:30]
    http_method_names = ["get"]
    template_name = "events/date_list.html"
    model = EventsList
    context_object_name = "page"

    def get_context_data(self, *args, **kwargs):
        context = super(PageEventsList, self).get_context_data(*args, **kwargs)
        context['events'] = EventDate.objects.filter(event__id=self.kwargs['pk']).order_by('date')
        return context

    # def get_context_data(self, *args, **kwargs):
    #     context = super(PageEventsList, self).get_context_data(*args, **kwargs)
    #     context['events'] = Event.objects.filter(location__slug=self.kwargs['slug'])
    #     return context


class EventDetailView(DetailView):    
    html_method_names = ["get"]
    template_name = "events/detail.html"
    models = EventDate, Event,
    context_object_name = "event"

    def get_queryset(self, **kwargs):
        return EventDate.objects.filter(id=self.kwargs['pk'])
    
    # def get_context_data(self, *args, **kwargs):
    #     context = super(EventDetailView, self).get_context_data(*args, **kwargs)
    #     context['master_event'] = Event.objects.filter(id = event_id)
        # context['page_reviews'] = PageReviews.objects.filter(page_name__slug=self.kwargs['slug']).order_by('-date')
        
        return context


class PageAddEventView(LoginRequiredMixin, CreateView):
    models = Event, Page
    form_class = EventCreateForm
    template_name = "events/add_event.html"
    success_message = "Your event was added successfully"
    # fields = (
    #         "title",
    #         "description",
    #         "image",
    #         "host_list",
    #     )
    success_url = reverse_lazy("events:events") 



    def form_valid(self, form):
        form.instance.location_id = self.kwargs.get('pk')        
        form.instance.organiser = self.request.user
        return super(PageAddEventView, self).form_valid(form)

    def get_object(self):
       return self.request.user
    
    def get_context_data(self, *args, **kwargs):
        context = super(PageAddEventView, self).get_context_data(*args, **kwargs)
        context['host_choices'] = PageHost.objects.filter(page_name_id=self.kwargs['pk'])
        return context
    
class AddEventDateView(LoginRequiredMixin, CreateView):
    models = EventDate
    form_class = EventAddDatesForm
    template_name = "events/add_date.html"
    # queryset = Event.objects.all()
    success_message = "Your event was added successfully"
    success_url = "/events/"

    def form_valid(self, form):
        form.instance.event_id = self.kwargs.get('pk')        
        form.instance.organiser = self.request.user
        return super(AddEventDateView, self).form_valid(form)

    def get_object(self):
       return self.request.user