from django.db.models.base import Model as Model
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from datetime import datetime

from pages.models import Page, PageHost
from profiles.models import Profile

from .models import MasterEvent, Event, ClubEvent

# uncommment this affter migration
from .forms import ClubEventCreateForm

# Create your views here.


class MasterEventList(ListView):
    paginate_by = 15
    html_method_names = ["get"]
    template_name = "event/date_list.html"
    models = MasterEvent
    context_object_name = "master_event"


class EventList(ListView):
    paginate_by = 15
    html_method_names = ["get"]
    template_name = "event/date_list.html"
    models = Event
    context_object_name = "event_list"
    today = datetime.now()
    queryset = Event.objects.filter(date__gt=today).order_by("date")[0:30]


class ClubAddEventView(LoginRequiredMixin, CreateView):
    model = ClubEvent
    form_class = ClubEventCreateForm
    template_name = "event/add_event.html"
    success_message = "Your event was added successfully"
    # fields = (
    #         "title",
    #         "description",
    #         "image",
    #     )
    success_url = reverse_lazy("events:events")

    def form_valid(self, form):
        form.instance.location_id = self.kwargs.get("pk")
        form.instance.organiser = self.request.user
        form.instance.event_type = "swingers-club-event"
        return super(ClubAddEventView, self).form_valid(form)

    def get_object(self):
        return self.request.user

    def get_context_data(self, *args, **kwargs):
        context = super(ClubAddEventView, self).get_context_data(*args, **kwargs)
        context["host_choices"] = PageHost.objects.filter(
            page_name_id=self.kwargs["pk"]
        )
        return context


class EventDetailView(DetailView):
    html_method_names = ["get"]
    template_name = "event/detail.html"
    models = Event, MasterEvent
    context_object_name = "event_date"

    def get_queryset(self, **kwargs):
        return Event.objects.filter(id=self.kwargs["pk"])
        # return EventHost.objects.all()
        # return EventHost.objects.filter(event_id=self.kwargs['pk'])
        #

    def get_context_data(self, *args, **kwargs):
        context = super(EventDetailView, self).get_context_data(*args, **kwargs)
        context["hosts"] = Profile.objects.filter(user__id=self.kwargs["pk"])
        print(context)
        return context
