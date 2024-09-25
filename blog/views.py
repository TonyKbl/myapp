from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from .models import Blog, Catagory, Tag
from profiles.models import Profile

class BlogCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Blog
    # form_class = PageCreateForm
    template_name = "blog/blog_add_edit_form.html"
    success_message = "Blog successfully added"
    success_url = "/blog/" 
    fields = ('catagory', 'title', 'article', 'header_image', 'tags')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)