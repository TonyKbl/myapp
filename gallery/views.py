from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from queryset_sequence import QuerySetSequence
from itertools import chain
from operator import attrgetter
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q

from .models import UserGallery
from profiles.models import Follow, Profile

# Create your views here.

class UserGalleryView(LoginRequiredMixin, DetailView):
    html_method_names = ["get"]
    template_name = "gallery/gallery.html"
    models = UserGallery, User, Profile
    context_object_name = "gallery"

    def get_context_data(self, *args, **kwargs):
        context = super(UserGalleryView, self).get_context_data(*args, **kwargs)
        # context['page_posts'] = PagePost.objects.filter(name__page_name=self.kwargs['slug'])
        context['gallery'] = UserGallery.objects.filter(owner__slug=self.kwargs['slug'])
        return context
    
    # def get_queryset(self):
    #     pass
        
    #     followed_users = self.request.user.following.all()      
    #     qs1 = Post.objects.filter(Q(author__in=followed_users.values('following'))) #your first qs

    #     followed_pages = self.request.user.page_following.all()
    #     qs2 = PagePost.objects.filter(Q(name__in=followed_pages.values('following')))  #your second qs
        
    #     queryset = sorted(chain(qs1,qs2),key=attrgetter('date'),reverse=True)
    #     return queryset
    