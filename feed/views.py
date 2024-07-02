from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Post

# Create your views here.

class HomePage(ListView):
    html_method_names = ["get"]
    template_name = "feed/homepage.html"
    models = Post
    context_object_name = "posts"
    queryset = Post.objects.all().order_by('-id')[0:30]

class ProfilePage(ListView):
    html_method_names = ["get"]
    template_name = "profile/feed.html"
    models = Post
    context_object_name = "posts"
    queryset = Post.objects.all().order_by('-id')[0:30]

class PostDetailView(DetailView):
    html_method_names = ["get"]
    template_name = "feed/detail.html"
    models = Post
    context_object_name = "post"
    queryset = Post.objects.all()


class CreateNewPost(CreateView):
    models = Post
    template_name = "feed/create.html"
    fields = ['text',"image"]
    queryset = Post.objects.all()
    success_url = "/"
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

