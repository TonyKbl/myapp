# from django.db.models.base import Model as Model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.db.models import Avg
from django.db.models.query import QuerySet
from django.http import Http404, HttpRequest, request
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.edit import UpdateView
from django.template import loader
from django.http import HttpResponse
from django.core.mail import send_mail

from feed.models import PagePost
from event.models import Event
from place_area.models import PostCode
from profiles.models import Profile

from .forms import (
    PageAddHostForm,
    PageClaimForm,
    ClubPageCreateForm,
    PageReviewForm,
    ClubPageUpdateForm,
    PageEmailForm,
)
from .models import ClaimPage, ClubPage, PageFollow, PageHost, PageReviews, Page


class PageListView(ListView):
    http_method_names = ["get"]
    template_name = "pages/list.html"
    model = Page
    context_object_name = "pages"

    def get_queryset(self):
        # ord = self.kwargs['ord']
        ord = self.request.GET.get("ord")
        if ord == "county":
            queryset = Page.objects.all().order_by("county", "page_name")
        elif ord == "region":
            queryset = Page.objects.all().order_by("region", "page_name")
        elif ord == "rating":
            queryset = Page.objects.all().order_by(PageReviews.page_name.Avg("rating"))
        else:
            queryset = Page.objects.all().order_by("page_name")

        # order = {"ord": ord}
        return queryset


class ClubPageListView(ListView):
    http_method_names = ["get"]
    template_name = "pages/club-list.html"
    model = ClubPage
    context_object_name = "pages"

    def get_queryset(self):
        # ord = self.kwargs['ord']
        ord = self.request.GET.get("ord")
        if ord == "county":
            queryset = ClubPage.objects.all().order_by("county", "page_name")
        elif ord == "region":
            queryset = ClubPage.objects.all().order_by("region", "page_name")
        elif ord == "rating":
            queryset = ClubPage.objects.all().order_by(
                PageReviews.page_name.Avg("rating")
            )
        else:
            queryset = ClubPage.objects.all().order_by("page_name")

        # order = {"ord": ord}
        return queryset


class ClubPageDetailView(DetailView):
    http_method_names = ["get"]
    template_name = "pages/detail.html"
    model = ClubPage
    context_object_name = "page"
    # slug_field = "slug"
    # slug_url_kwarg = "slug"


class ClubPageCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = ClubPage
    form_class = ClubPageCreateForm
    template_name = "pages/page_add_edit_form.html"
    success_message = "Page successfully added"
    success_url = "/pages/"

    def form_valid(self, form):
        try:
            location = PostCode.objects.get(postcode=form.instance.post_code)
        except:
            raise ValidationError("Please enter a valid Postcode")
        # print(location)
        form.instance.lat = location.lat
        form.instance.lon = location.lon
        form.instance.loc = Point(float(location.lon), float(location.lat))
        form.instance.user = self.request.user
        form.instance.page_type = "Swingers Club"
        return super().form_valid(form)

    # def get_success_url(self):
    #     slug = self.kwargs["slug"]
    #     page_type = self.kwargs["page_type"]
    #     return reverse_lazy("pages:detail", kwargs={"page_type": page_type, "slug": slug})


class ClubPageUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ClubPage
    form_class = ClubPageUpdateForm
    template_name = "pages/page_add_edit_form.html"
    success_message = "Page successfully updated"

    # def get_object(self):
    #    return self.request.user

    def get_object(self, queryset=None):
        obj = ClubPage.objects.get(id=self.kwargs.get("pk"))
        return obj

    def get_success_url(self):
        slug = self.kwargs["slug"]
        page_type = self.kwargs["page_type"]
        return reverse_lazy(
            "pages:detail", kwargs={"page_type": page_type, "slug": slug}
        )

    def form_valid(self, form):
        try:
            location = PostCode.objects.get(postcode=form.instance.post_code)
            form.instance.lat = location.lat
            form.instance.lon = location.lon
            form.instance.loc = Point(float(location.lon), float(location.lat))
        except:
            alert = "Please enter a valid postcode"
        return super().form_valid(form)


class PageFeedView(LoginRequiredMixin, DetailView):
    http_method_names = ["get"]
    template_name = "pages/feed.html"
    model = Page

    def get_context_data(self, *args, **kwargs):
        page_size = 15
        item_cnt = PagePost.objects.filter(name__slug=self.kwargs["slug"]).count()
        total_pages = (item_cnt + page_size - 1) // page_size

        try:
            page_number = int(self.request.GET.get("pg", 1))

            if 1 <= page_number <= total_pages:
                start_index = (page_number - 1) * page_size
                end_index = page_number * page_size

            else:
                start_index = 1 * page_size
                end_index = page_number * page_size

        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            raise Http404

        context = super(PageFeedView, self).get_context_data(*args, **kwargs)
        context["page_posts"] = PagePost.objects.filter(
            name__slug=self.kwargs["slug"]
        ).order_by("-date")[start_index:end_index]
        context["total_pages"] = str(total_pages)
        context["page_number"] = str(page_number)
        context["prev"] = str(page_number - 1)
        context["next"] = str(page_number + 1)
        return context


class PageEventsView(LoginRequiredMixin, DetailView):
    http_method_names = ["get"]
    template_name = "pages/events.html"
    model = Page

    def get_context_data(self, *args, **kwargs):
        page_size = 15
        item_cnt = Event.objects.filter(page__slug=self.kwargs["slug"]).count()
        total_pages = (item_cnt + page_size - 1) // page_size

        try:
            page_number = int(self.request.GET.get("pg", 1))

            if 1 <= page_number <= total_pages:
                start_index = (page_number - 1) * page_size
                end_index = page_number * page_size

            else:
                start_index = 1 * page_size
                end_index = page_number * page_size

        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            raise Http404

        context = super(PageEventsView, self).get_context_data(*args, **kwargs)
        context["page_events"] = Event.objects.filter(
            page__slug=self.kwargs["slug"]
        ).order_by("-date")[start_index:end_index]
        context["total_pages"] = str(total_pages)
        context["page_number"] = str(page_number)
        context["prev"] = str(page_number - 1)
        context["next"] = str(page_number + 1)
        return context


# class SendClubEmail(self, *args, **kwargs):
#     # obj_id = instance._id

#     message = """A message has been send from clubswing.co.uk contact page on your profile

#     Page - {pg_name}
#     Name - {name}
#     Email - {email}
#     Subject - {subject}

#     Message
#     =======
#     {message}

#     """.format(
#         pg_name=self.kwargs["slug"],
#         name=request.GET.get("name"),
#         email=request.GET.get("email"),
#         subject=request.GET.get("subject"),
#         message=request.GET.get("message"),
#     )
#     subject = request.GET.get("subject")
#     email = request.GET.get("email")
#     name = request.GET.get("name")

#     send_mail(
#         subject,
#         message,
#         name,
#         [email],
#         fail_silently=False,
#     )


# def email_view(slug):
#     name = request.POST.get("full_name", False)
#     email = request.POST.get("email", False)
#     subject = request.POST.get("subject", False)
#     message = request.POST.get("message", False)
#     form = PageEmailForm()
#     if request.method == "POST":
#         form = PageEmailForm(request.POST)
#     if form.is_valid():
#         send_club_email(name, email, subject, message)
#         template = loader.get_template("./templates/pages/thankyoumsg.html")
#         return HttpResponse(template.render({}, request))
#     template = loader.get_template("./templates/pages/contact.html")
#     return HttpResponse(template.render({"form": form}, request))


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
        context["page_reviews"] = PageReviews.objects.filter(
            page_name__slug=self.kwargs["slug"]
        ).order_by("-date")
        return context


class PageAddReviewView(LoginRequiredMixin, CreateView):
    model = PageReviews
    form_class = PageReviewForm
    template_name = "pages/add_review.html"
    # queryset = PageReviews.objects.all()
    success_message = "Your review was added successfully"
    success_url = "/"

    def form_valid(self, form):
        form.instance.page_name_id = self.kwargs.get("pk")
        form.instance.author = self.request.user
        return super(PageAddReviewView, self).form_valid(form)

    def get_object(self):
        return self.request.user


class PageAddHostView(LoginRequiredMixin, CreateView):
    model = PageHost
    form_class = PageAddHostForm
    template_name = "pages/add_host.html"
    # queryset = PageReviews.objects.all()
    success_message = "Your host was added successfully"
    success_url = "/"

    def form_valid(self, form):
        form.instance.page_name_id = self.kwargs.get("pk")
        return super(PageAddHostView, self).form_valid(form)

    def get_queryset(self):
        qs = PageFollow.follower.filter(following=self.kwargs.get("pk"))
        return qs

    def get_object(self):
        return self.request.user


class PageAddClaimView(LoginRequiredMixin, CreateView):
    model = ClaimPage
    form_class = PageClaimForm
    template_name = "pages/add_claim.html"
    # queryset = PageReviews.objects.all()
    success_message = "Your claim was sent successfully"
    success_url = "/"

    def form_valid(self, form):
        form.instance.page_claimed_id = self.kwargs.get("pk")
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
    if request.method == "POST":
        follow_relationship, created = PageFollow.objects.get_or_create(
            follower=request.user, following=tp
        )
        if created:
            messages.success(request, "You are now following a new page")
        if not created:
            follow_relationship.delete()
            messages.warning(request, "You just unfollowed a page")

    return redirect("/", page=Page.slug)
