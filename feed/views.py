from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post

# Create your views here.

class HomePage(LoginRequiredMixin, ListView):
    html_method_names = ["get"]
    template_name = "feed/homepage.html"
    models = Post
    context_object_name = "posts"
    queryset = Post.objects.all().order_by('-id')[0:30]

class PostDetailView(LoginRequiredMixin, DetailView):
    html_method_names = ["get"]
    template_name = "feed/detail.html"
    models = Post
    context_object_name = "post"
    queryset = Post.objects.all()


class CreateNewPost(LoginRequiredMixin, CreateView):
    models = Post
    template_name = "feed/create.html"
    fields = ['text',"image"]
    queryset = Post.objects.all()
    success_url = "/"
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

