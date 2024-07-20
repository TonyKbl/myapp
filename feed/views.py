from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from queryset_sequence import QuerySetSequence
from itertools import chain
from operator import attrgetter

from .models import Post, PagePost

# Create your views here.

class HomePage(LoginRequiredMixin, ListView):
    html_method_names = ["get"]
    template_name = "feed/homepage.html"
    models = Post, PagePost
    context_object_name = "posts"
    # queryset = Post.objects.all().order_by('-id')[0:30]
    # queryset = QuerySetSequence(Post.objects.all(), PagePost.objects.all())

    def get_queryset(self):
        qs1 = Post.objects.all() #your first qs
        qs2 = PagePost.objects.all()  #your second qs
        #you can add as many qs as you want
        queryset = sorted(chain(qs1,qs2),key=attrgetter('date'),)
        return queryset

# Import QuerySetSequence
# from queryset_sequence import QuerySetSequence

# Create QuerySets you want to chain.
# from .models import SomeModel, OtherModel

# Chain them together.

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

    # def form_valid(self, form):        
    #     self.object = self.get_object()
    #     page = self.object[0]
    #     # new_page_post = kwargs.pop('page', None)
    #     print("page = " + page)
    #     # super(CreateNewPagePost, self).form_valid(*args, **kwargs)
    #     if page:
    #         self.fields['feed_pagepost.author'].initial = page
    #     # form.instance.page = 
    #     return super().form_valid(form)

