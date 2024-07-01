from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from .models import Page
from profiles.models import Profile
from .forms import PageUpdateForm, PageCreateForm

class PageDetailView(DetailView):
    http_method_names = ["get"]
    template_name = "pages/detail.html"
    model = Profile
    context_object_name = "user"
    slug_field = "username"
    slug_url_kwarg = "username"
    

class PageCreateView(CreateView):
    model = Page
    form_class = PageCreateForm
    template_name = "pages/page_create_form.html"
    success_url = "/"

class PageUpdateView(UpdateView):
    model = Page
    form_class = PageUpdateForm
    template_name = "pages/page_update_form.html"
    success_url = "/"

   # def get_object(self):
    #    return self.request.user
    
    
    
    def get_object(self, queryset=None):
        obj = Page.objects.get(user=self.request.user)
        return obj
    