from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect

from .models import Profile, Follow
from .forms import ProfileUpdateForm
from feed.models import Post

class ProfileDetailView(LoginRequiredMixin, DetailView):
    http_method_names = ["get"]
    template_name = "profiles/detail.html"
    model = User
    context_object_name = "user"
    slug_field = "username"
    slug_url_kwarg = "username"

    target_user = id

    context = {'target_user':target_user}
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
    

def follow(request, username):
    target_user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        if request.user != target_user:
            follow_relationship,  created = Follow.objects.get_or_create(follower = request.user, following = target_user)
            if not created:
                follow_relationship.delete()

    return redirect('/', username=username)

