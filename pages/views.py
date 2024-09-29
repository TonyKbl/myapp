from django.db.models.base import Model as Model
from django.db.models import Avg
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpRequest, request, Http404
from django.core.paginator import Paginator

from .models import Page, PageFollow, PageReviews, ClaimPage, PageHost
from feed.models import PagePost
from profiles.models import Profile
from .forms import PageUpdateForm, PageCreateForm, PageReviewForm, PageClaimForm, PageAddHostForm


class PageListView(ListView):    
    http_method_names = ["get"]
    template_name = "pages/list.html"
    model = Page
    context_object_name = "pages"
   
    
    def get_queryset(self):
        # ord = self.kwargs['ord']
        ord = self.request.GET.get('ord')
        if ord == 'county':
            queryset = Page.objects.all().order_by('county', 'page_name')
        elif ord == 'region':             
            queryset = Page.objects.all().order_by('region', 'page_name')
        elif ord == 'rating':
            queryset = Page.objects.all().order_by(PageReviews.page_name.Avg('rating'))
        else:
            queryset = Page.objects.all().order_by('page_name')
        return self.Avg('rating')
                
        
        order = {"ord": ord}
        return (queryset)


class PageDetailView(DetailView):
    http_method_names = ["get"]
    template_name = "pages/detail.html"
    model = Page
    context_object_name = "page"
    # slug_field = "slug"
    # slug_url_kwarg = "slug"
    

class PageCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Page
    form_class = PageCreateForm
    template_name = "pages/page_add_edit_form.html"
    success_message = "Page successfully added"
    success_url = "/pages/" 

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PageUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Page
    form_class = PageUpdateForm
    template_name = "pages/page_add_edit_form.html"    
    success_message = "Page successfully updated"

    def get_object(self):
       return self.request.user
    
    def get_object(self, queryset=None):
        obj = Page.objects.get(id=self.kwargs.get('pk'))
        return obj
    
    def get_success_url(self):
        slug = self.kwargs["slug"]
        page_type = self.kwargs["page_type"]
        return reverse_lazy("pages:detail", kwargs={"page_type": page_type, "slug": slug})
    

class PageFeedView(LoginRequiredMixin, DetailView):
    http_method_names = ["get"]
    template_name = "pages/feed.html"
    model = Page

    def get_context_data(self, *args, **kwargs):
        page_size = 15
        item_cnt = PagePost.objects.filter(name__slug=self.kwargs['slug']).count()
        total_pages = (item_cnt + page_size - 1) // page_size

        try:
            page_number = int(self.request.GET.get('pg', 1))
                        
            if 1 <= page_number <= total_pages:
                start_index = (page_number - 1) * page_size
                end_index = page_number * page_size
                
            else:
                raise Http404
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            raise Http404


        context = super(PageFeedView, self).get_context_data(*args, **kwargs)
        context['page_posts'] = PagePost.objects.filter(name__slug=self.kwargs['slug']).order_by('-date')[start_index:end_index]
        context['total_pages'] = str(total_pages)
        context['page_number'] = str(page_number)
        context['prev'] = str(page_number-1)
        context['next'] = str(page_number+1)
        return context
    
  

#### START OF COOD CODE #####

# class PageFeedView(LoginRequiredMixin, DetailView):
#     http_method_names = ["get"]
#     template_name = "pages/feed.html"
#     model = Page
#     context_object_name = "page"

#     def get_context_data(self, *args, **kwargs):
#         context = super(PageFeedView, self).get_context_data(*args, **kwargs)
#         context['page_posts'] = PagePost.objects.filter(name__slug=self.kwargs['slug']).order_by('-date')
#         return context


class PageReviewsView(DetailView): 
    http_method_names = ["get"]
    template_name = "pages/reviews.html"
    model = Page
    context_object_name = "page"

    def get_context_data(self, *args, **kwargs):
        context = super(PageReviewsView, self).get_context_data(*args, **kwargs)
        context['page_reviews'] = PageReviews.objects.filter(page_name__slug=self.kwargs['slug']).order_by('-date')
        return context


class PageAddReviewView(LoginRequiredMixin, CreateView):
    models = PageReviews
    form_class = PageReviewForm
    template_name = "pages/add_review.html"
    # queryset = PageReviews.objects.all()    
    success_message = "Your review was added successfully"
    success_url = "/"

    def form_valid(self, form):
        form.instance.page_name_id = self.kwargs.get('pk')        
        form.instance.author = self.request.user
        return super(PageAddReviewView, self).form_valid(form)

    def get_object(self):
       return self.request.user

class PageAddHostView(LoginRequiredMixin, CreateView):
    models = PageHost
    form_class = PageAddHostForm
    template_name = "pages/add_host.html"
    # queryset = PageReviews.objects.all()    
    success_message = "Your host was added successfully"
    success_url = "/"

    def form_valid(self, form):
        form.instance.page_name_id = self.kwargs.get('pk')
        return super(PageAddHostView, self).form_valid(form)

    def get_object(self):
       return self.request.user

class PageAddClaimView(LoginRequiredMixin, CreateView):
    models = ClaimPage
    form_class = PageClaimForm
    template_name = "pages/add_claim.html"
    # queryset = PageReviews.objects.all()    
    success_message = "Your claim was sent successfully"
    success_url = "/"

    def form_valid(self, form):
        form.instance.page_claimed_id = self.kwargs.get('pk')        
        form.instance.claimant = self.request.user
        return super(PageAddClaimView, self).form_valid(form)

    def get_object(self):
       return self.request.user


# class PageGalleryView(LoginRequiredMixin, DetailView): 
#     http_method_names = ["get"]
#     template_name = "pages/gallery.html"
#     model = Page
#     context_object_name = "page"

#     def get_context_data(self, *args, **kwargs):
#         context = super(PageGalleryView, self).get_context_data(*args, **kwargs)
#         context['page_gallery'] = PageGallery.objects.filter(page_name__slug=self.kwargs['slug']).order_by('-date')
#         return context
    

@login_required
def page_follow(request, slug):
    tp = get_object_or_404(Page, slug=slug)
    if request.method == 'POST':
        follow_relationship,  created = PageFollow.objects.get_or_create(follower = request.user, following = tp)
        if created: 
            messages.success(request, "You are now following a new page")
        if not created:
            follow_relationship.delete()
            messages.warning(request, "You just unfollowed a page")


    return redirect('/', page=Page.slug)