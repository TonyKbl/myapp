from django.shortcuts import render
from profiles.models import Profile
from pages.models import Page

# from events.models import MasterEvent, EventDate
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView, CreateView


# Create your views here.
class SearchAll(LoginRequiredMixin, ListView):
    http_method_names = ["get"]
    model = Profile
    template_name = "search/list.html"
    # context_object_name = "profiles"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # ord = self.kwargs['ord']
        q = self.request.GET.get("q")
        context["profiles"] = Profile.objects.filter(
            display_name__icontains=q
        ).order_by("-date_joined")[:3]
        context["pages"] = Page.objects.filter(page_name__icontains=q).order_by(
            "-page_updated"
        )[:3]
        # uncommment this affter migration
        # context["events"] = MasterEvent.objects.filter(title__icontains=q)[:3]

        # elif q == 'updated':
        #     queryset = Profile.objects.all().order_by('-last_updated')
        # else:
        #     queryset = Profile.objects.all().order_by('user')

        return context
