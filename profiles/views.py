from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from feed.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Profile
from .forms import ProfileUpdateForm

class ProfileDetailView(LoginRequiredMixin, DetailView):
    http_method_names = ["get"]
    template_name = "profiles/detail.html"
    model = User
    context_object_name = "user"
    slug_field = "username"
    slug_url_kwarg = "username"

    # if(profile_page):
    #     pass
    

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = "profiles/profile_update_form.html"
    success_url = "/"

    def get_object(self):
       return self.request.user
    
    
    
    def get_object(self, queryset=None):
        obj = Profile.objects.get(user=self.request.user)
        return obj


# class ProfileFeedView(ListView):

    # html_method_names = ["get"]
    # template_name = "profile/feed.html"
    # models = Post
    # context_object_name = "posts"
    # queryset = Post.objects.all().order_by('-id')[0:30]

class ProfileFeedView(LoginRequiredMixin, DetailView): 
    http_method_names = ["get"]
    template_name = "profiles/feed.html"
    model = User
    context_object_name = "user"
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileFeedView, self).get_context_data(*args, **kwargs)
        context['posts'] = Post.objects.filter(author__username=self.kwargs['username'])
        return context

class ProfileGalleryView(LoginRequiredMixin, DetailView): 
    http_method_names = ["get"]
    template_name = "profiles/gallery.html"
    model = User
    context_object_name = "user"
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileGalleryView, self).get_context_data(*args, **kwargs)
        context['posts'] = Post.objects.filter(author__username=self.kwargs['username'])
        return context