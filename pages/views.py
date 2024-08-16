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

from .models import Page, PageFollow, PageReviews
from feed.models import PagePost
from profiles.models import Profile
from .forms import PageUpdateForm, PageCreateForm, PageReviewForm

class PageListView(ListView):    
    http_method_names = ["get"]
    template_name = "pages/list.html"
    model = Page
    context_object_name = "pages"
    queryset = Page.objects.all().order_by('-page_updated')[0:30]

    


class PageDetailView(DetailView):
    http_method_names = ["get"]
    template_name = "pages/detail.html"
    model = Page
    context_object_name = "page"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    target_page = id

    context = {'target_page':target_page}
    

class PageCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Page
    form_class = PageCreateForm
    template_name = "pages/page_add_edit_form.html"
    # fields = ["page_type", "cover_image", "image"]
    success_message = "Page successfully added"
    # slug_url_kwarg = "name"
    # slug = slugify(name) 
    success_url = "/pages/" 

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    # def get_success_url(self):
    #     # slug = self.kwargs["slug"]
    #     # n = form.instance.user
    #     return reverse_lazy("pages:detail", {"slug":self.slug_field})


class PageUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Page
    form_class = PageUpdateForm
    template_name = "pages/page_add_edit_form.html"    
    success_message = "Page successfully updated"
    # success_url = "/page/ slug:slug"

    def get_object(self):
       return self.request.user
    
    def get_object(self, queryset=None):
        obj = Page.objects.get(id=self.kwargs.get('pk'))
        return obj
    
    def get_success_url(self):
        slug = self.kwargs["slug"]
        return reverse_lazy("pages:detail", kwargs={"slug": slug})
    

class PageFeedView(LoginRequiredMixin, DetailView): 
    http_method_names = ["get"]
    template_name = "pages/feed.html"
    model = Page
    context_object_name = "page"
    # slug_field = "name"
    # slug_url_kwarg = "name"

    def get_context_data(self, *args, **kwargs):
        context = super(PageFeedView, self).get_context_data(*args, **kwargs)
        # context['page_posts'] = PagePost.objects.filter(name__page_name=self.kwargs['slug'])
        context['page_posts'] = PagePost.objects.filter(name__slug=self.kwargs['slug'])
        return context


class PageReviewsView(LoginRequiredMixin, DetailView): 
    http_method_names = ["get"]
    template_name = "pages/reviews.html"
    model = Page
    context_object_name = "page"
    # slug_field = "name"
    # slug_url_kwarg = "name"

    def get_context_data(self, *args, **kwargs):
        context = super(PageReviewsView, self).get_context_data(*args, **kwargs)
        context['page_reviews'] = PageReviews.objects.filter(page_name__slug=self.kwargs['slug'])
        return context

    def avg_rating(self, *args, **kwargs):
        context2 = super(PageReviewsView, self).get_context_data(*args, **kwargs)
        # context2['page_avg_reviews'] = PageReviews.objects.filter(page__slug=self.kwargs['slug']).annotate(avg_rating=Avg('rating'))
        context2['page_avg_reviews'] = PageReviews.objects.annotate(avg_rating=Avg('rating'))
        return context2
    
class PageAddReviewView(LoginRequiredMixin, CreateView):
    models = PageReviews
    form_class = PageReviewForm
    template_name = "pages/add_review.html"
    
    # fields = ['rating',"text"]
    queryset = PageReviews.objects.all()    
    success_message = "Your review was added successfully"
    success_url = "/"

    def form_valid(self, form):
        # form.instance.author_id = self.kwargs.get('id')
        form.instance.page_name_id = self.kwargs.get('pk')        
        form.instance.author = self.request.user
        print(self.kwargs)    
        print(form.instance.page_name_id)    
        print(form.instance.author)    
        # form.instance.user = self.request.user
        return super(PageAddReviewView, self).form_valid(form)

    def get_object(self):
       return self.request.user
    
    # def get_object(self, slug, queryset=None):
    #     # obj = Page(slug=slug)
    #     obj = Page.objects.get(user=self.request.user)
    #     return obj

    # models = PagePost
    # template_name = "feed/create.html"
    # fields = ['text',"image"]
    # queryset = PagePost.objects.all()
    # success_url = "/"
    
    # def form_valid(self, form):
    #     # form.instance.author_id = self.kwargs.get('id')
    #     form.instance.name_id = self.kwargs.get('id')        
    #     form.instance.author = self.request.user
    #     form.instance.post_type = "page"
    #     return super(CreateNewPagePost, self).form_valid(form)




@login_required
def page_follow(request, slug):
    tp = get_object_or_404(Page, slug=slug)
    if request.method == 'POST':
        follow_relationship,  created = PageFollow.objects.get_or_create(follower = request.user, following = tp)
        if created: messages.success(request, "You are now following a new page")

        if not created:
            follow_relationship.delete()
            messages.warning(request, "You just unfollowed a page")


    return redirect('/', page=Page.slug)