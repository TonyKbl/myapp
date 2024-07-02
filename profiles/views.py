from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from feed.models import Post

from .models import Profile
from .forms import ProfileUpdateForm

class ProfileDetailView(DetailView):
    http_method_names = ["get"]
    template_name = "profiles/detail.html"
    model = User
    context_object_name = "user"
    slug_field = "username"
    slug_url_kwarg = "username"
    

class ProfileUpdateView(UpdateView):
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

class ProfileFeedView(ListView): 
    def get_queryset(self):
        return Post.objects.filter(author__username=self.kwargs['username'])
    html_method_names = ["get"]  
    template_name = "profiles/feed.html"
    # model = Post   
    context_object_name = "posts"
    # queryset=Post.objects.filter(author__username = User.username )
    # # queryset = Post.objects.all().order_by('-id')[0:30]


    
    