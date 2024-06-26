from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from .models import Page
from profiles.models import Profile
from .forms import PageUpdateForm, PageCreateForm

class PageListView(ListView):
    pass

class PageDetailView(DetailView):
    http_method_names = ["get"]
    template_name = "pages/detail.html"
    model = Page
    context_object_name = "page"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    

class PageCreateView(CreateView):
    model = Page
    form_class = PageCreateForm
    template_name = "pages/page_create_form.html"
    # fields = ["page_type", "cover_image", "image"]
    success_url = "/"


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    



class PageUpdateView(UpdateView):
    pass
#     model = Page
#     form_class = PageUpdateForm
#     template_name = "pages/page_update_form.html"
#     success_url = "/"

#    # def get_object(self):
#     #    return self.request.user
    
    
    
#     def get_object(self, queryset=None):
#         obj = Page.objects.get(user=self.request.user)
#         return obj
    