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

from .models import Post, PagePost
from profiles.models import Follow

# Create your views here.

class HomePage(LoginRequiredMixin, ListView):
    html_method_names = ["get"]
    template_name = "feed/homepage.html"
    models = User, Post, PagePost
    context_object_name = "posts"
    # queryset = Post.objects.all().order_by('-id')[0:30]
    # queryset = QuerySetSequence(Post.objects.all(), PagePost.objects.all())

    def get_queryset(self):
        print(self.request.user.id)
        followed_users = self.request.user.following.all()
        qs1 = Post.objects.filter(Q(author__in=followed_users.values('following'))) #your first qs
        # qs1 = Post.objects.all()
        qs2 = PagePost.objects.all()  #your second qs
        #you can add as many qs as you want
        queryset = sorted(chain(qs1,qs2),key=attrgetter('date'),reverse=True)
        return queryset
    

class PostDetailView(LoginRequiredMixin, DetailView):    
    html_method_names = ["get"]
    template_name = "feed/detail.html"
    models = User, Post, PagePost,
    context_object_name = "post"

    def get_queryset(self, **kwargs):
        if self.kwargs['page_type'] == 'profile':
            return Post.objects.filter(author=self.request.user)
        elif self.kwargs['page_type'] == 'page':
            # print("kwargs: ", kwargs)
            return PagePost.objects.filter(id=self.kwargs['pk'])


class CreateNewPost(LoginRequiredMixin, CreateView):
    models = Post
    template_name = "feed/create.html"
    fields = ['text',"image"]
    queryset = Post.objects.all()
    success_url = "/"
    
    def form_valid(self, form):
        form.instance.author = self.request.user        
        form.instance.post_type = "profile"
        return super().form_valid(form)

class CreateNewPagePost(LoginRequiredMixin, CreateView):
    models = PagePost
    template_name = "feed/create.html"
    fields = ['text',"image"]
    queryset = PagePost.objects.all()
    success_url = "/"
    
    def form_valid(self, form):
        # form.instance.author_id = self.kwargs.get('id')
        form.instance.name_id = self.kwargs.get('id')        
        form.instance.author = self.request.user
        form.instance.post_type = "page"
        return super(CreateNewPagePost, self).form_valid(form)

