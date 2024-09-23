from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

from .models import Profile, Follow
from .forms import ProfileUpdateForm, ProfileCoverUpdateForm, ProfileAvatarUpdateForm,  ProfileGalleryCreateForm
from feed.models import Post
from gallery.models import UserGallery

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
    # success_url = reverse('profile:detail', user.username)
    
    def get_success_url(self):
        return reverse("profiles:detail", kwargs={'username': self.request.user})

    def get_object(self):
       return self.request.user
    
    def get_object(self, queryset=None):
        obj = Profile.objects.get(user=self.request.user)
        return obj


class CoverImageUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileCoverUpdateForm
    template_name = "profiles/cover_update_form.html"
    
    def get_success_url(self):
        return reverse("profiles:detail", kwargs={'username': self.request.user})
   
    def get_object(self):
        return self.request.user    
        
    def get_object(self, queryset=None):
        obj = Profile.objects.get(user=self.request.user)
        return obj  


class AvatarImageUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileAvatarUpdateForm
    template_name = "profiles/avatar_update_form.html"
    success_url = "/pages/"
       
    def get_success_url(self):
        return reverse("profiles:detail", kwargs={'username': self.request.user})

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

    target_user = id
    context = {'target_user':target_user}

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileFeedView, self).get_context_data(*args, **kwargs)
        context['posts'] = Post.objects.filter(author__username=self.kwargs['username']).order_by('-date')
        return context

class ProfileGalleryView(LoginRequiredMixin, DetailView): 
    http_method_names = ["get"]
    template_name = "profiles/gallery.html"
    model = User
    context_object_name = "user"
    slug_field = "username"
    slug_url_kwarg = "username"

    target_user = id
    context = {'target_user':target_user}

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileGalleryView, self).get_context_data(*args, **kwargs)
        context['images'] = UserGallery.objects.filter(owner__username=self.kwargs['username'])
        return context


class ProfileAddGalleryView(LoginRequiredMixin, CreateView):
    model = UserGallery
    form_class = ProfileGalleryCreateForm
    template_name = "profiles/gallery_create_form.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
    def get_object(self):
       return self.request.user    
        
    def get_success_url(self):
        return reverse("profiles:gallery", kwargs={'username': self.request.user})

    # def get_object(self, queryset=None):
    #     obj = Profile.objects.get(user=self.request.user)
    #     return obj
    

def follow(request, username):
    target_user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        if request.user != target_user:
            follow_relationship,  created = Follow.objects.get_or_create(follower = request.user, following = target_user)
            if created: 
                messages.success(request, "You are now following a new user")
            if not created:
                follow_relationship.delete()
                messages.warning(request, "You have stopped following a user")

    return redirect('profiles:detail', username=username)

