from django.db.models.base import Model as Model
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, FormView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from pages.models import Page, PageHost
from profiles.models import Profile

from .models import MasterEvent, Event, ClubEvent, EventHost, Guestlist, Meet

from .forms import (
    ClubEventCreateForm,
    GuestlistCreateForm,
    GuestlistDeleteForm,
    EventAddDatesForm,
    PrivateMeetAddForm,
)


# Create your views here.


class MasterEventList(ListView):
    paginate_by = 15
    html_method_names = ["get"]
    template_name = "event/list.html"
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


class PrivateMeetListView(ListView):
    paginate_by = 15
    html_method_names = ["get"]
    template_name = "event/meet-list.html"
    models = Meet
    context_object_name = "event_list"
    today = datetime.now()
    queryset = Meet.objects.filter(date__gt=today).order_by("date")[0:30]


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


class PrivateMeetAddView(LoginRequiredMixin, CreateView):
    model = Meet
    form_class = PrivateMeetAddForm
    template_name = "event/add_meet.html"
    success_message = "Your event was added successfully"
    # fields = (
    #         "title",
    #         "description",
    #         "image",
    #     )
    success_url = reverse_lazy("events:events")

    def form_valid(self, form):
        form.instance.organiser = self.request.user
        form.instance.event_type = "private-meet"
        form.instance.private = "0"
        return super(PrivateMeetAddView, self).form_valid(form)

    def get_object(self):
        return self.request.user


class EventDetailView(DetailView):
    html_method_names = ["get"]
    template_name = "event/detail.html"
    models = MasterEvent
    context_object_name = "event_date"

    def get_queryset(self, **kwargs):
        ev = Event.objects.filter(id=self.kwargs["pk"])
        return ev
        # return EventHost.objects.all()
        # return EventHost.objects.filter(event_id=self.kwargs['pk'])
        #

    def get_context_data(self, *args, **kwargs):
        context = super(EventDetailView, self).get_context_data(*args, **kwargs)
        event = Event.objects.get(id=self.kwargs["pk"])
        master_event = MasterEvent.objects.get(master_event=event)
        try:
            context["guest"] = Guestlist.objects.get(
                event=event, guest=self.request.user.id
            )
        except:
            context["guest"] = None

        context["hosts"] = EventHost.objects.filter(event=master_event)
        print(context)
        return context


class ClubAddGuestlistView(LoginRequiredMixin, CreateView):
    model = Guestlist
    form_class = GuestlistCreateForm
    template_name = "event/add_guestlist.html"
    success_message = "Your were added successfully"
    success_url = reverse_lazy("events:events")

    def form_valid(self, form):
        form.instance.event_id = self.kwargs.get("pk")
        form.instance.guest = self.request.user
        form.instance.profile_type = self.request.user.profile.profile_type
        return super(ClubAddGuestlistView, self).form_valid(form)

    def get_object(self):
        return self.request.guest


class ClubDeleteGuestlistView(LoginRequiredMixin, DeleteView):
    model = Guestlist
    form_class = GuestlistDeleteForm
    template_name = "event/remove_guestlist.html"
    success_message = "Your were removed successfully"
    success_url = reverse_lazy("events:events")

    def form_valid(self, form):
        form.instance.event_id = self.kwargs.get("pk")
        form.instance.guest = self.request.user
        return super(ClubDeleteGuestlistView, self).form_valid(form)


class PageEventsList(ListView):
    # html_method_names = ["get"]
    # template_name = "events/list.html"
    # models = Events
    # context_object_name = "events"
    # queryset = Events.objects.all().order_by('-id')[0:30]
    http_method_names = ["get"]
    template_name = "event/master-events.html"
    model = Page
    context_object_name = "event"

    def get_context_data(self, *args, **kwargs):
        context = super(PageEventsList, self).get_context_data(*args, **kwargs)
        context["event"] = ClubEvent.objects.filter(
            location__id=self.kwargs["pk"]
        ).order_by("id")
        return context


class AddEventDateView(LoginRequiredMixin, CreateView):
    models = Event
    form_class = EventAddDatesForm
    template_name = "event/add_date.html"
    # queryset = Event.objects.all()
    success_message = "Your event was added successfully"
    success_url = "/events.html"

    def form_valid(self, form):
        form.instance.event_id = self.kwargs.get("pk")
        form.instance.organiser = self.request.user
        return super(AddEventDateView, self).form_valid(form)

    def get_object(self):
        return self.request.user


# @login_required
# def page_follow(request, pk):
#     tp = get_object_or_404(Event, id=pk)
#     if request.method == "POST":
#         guestlist_relationship, created = Guestlist.objects.get_or_create(
#             guest=request.user, event=tp
#         )
#         if created:
#             messages.success(request, "You are now on the guestlist")
#         if not created:
#             guestlist_relationship.delete()
#             messages.warning(request, "You are now removed from the guestlist")

#     return redirect("/", page=Page.slug)
