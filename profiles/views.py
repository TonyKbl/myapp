# from django.db.models.base import Model as Model
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

from .models import Profile, Follow, LookingFor, Interest
from place_area.models import OuterPostCode
from .forms import (
    ProfileUpdateForm,
    ProfileCoverUpdateForm,
    ProfileAvatarUpdateForm,
    ProfileGalleryCreateForm,
    SetProfileTypeForm,
    Profile2ndPersonForm,
    Profile1stPersonForm,
    LookingForUpdateForm,
    InterestUpdateForm,
)
from feed.models import Post
from gallery.models import UserGallery


class ProfileDetailView(LoginRequiredMixin, DetailView):
    http_method_names = ["get"]
    template_name = "profiles/detail.html"
    model = User
    context_object_name = "user"
    slug_field = "username"
    slug_url_kwarg = "username"

    target_user = id

    context = {"target_user": target_user}

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)

        # context['something'] =Book.objects.filter(pk=self.kwargs.get('pk'))
        # user = User.objects.filter(username = context)
        # context['lookingfor'] = LookingFor.objects.get(user=self.kwargs.get('username'))
        # context['lookingfor'] = LookingFor.objects.get(user=self.kwargs.get['id'])

        context["lookingfor"] = LookingFor.objects.get(
            user__username=self.kwargs["username"]
        )
        context["interests"] = Interest.objects.filter(
            user__username=self.kwargs["username"]
        )

        # context["target_user"] = self.request.user
        return context

    # if(profile_page):
    #     pass


class ProfileList(LoginRequiredMixin, ListView):
    http_method_names = ["get"]
    model = Profile
    template_name = "profiles/list.html"
    context_object_name = "profiles"

    def get_queryset(self):
        # ord = self.kwargs['ord']
        ord = self.request.GET.get("ord")
        if ord == "new":
            queryset = Profile.objects.all().order_by("-date_joined")
        elif ord == "updated":
            queryset = Profile.objects.all().order_by("-last_updated")
        else:
            queryset = Profile.objects.all().order_by("user")

        return queryset


class LookingForUpdateView(LoginRequiredMixin, UpdateView):
    model = LookingFor
    form_class = LookingForUpdateForm
    template_name = "profiles/Looking_for_update_form.html"

    def get_success_url(self):
        return reverse("profiles:detail", kwargs={"username": self.request.user})

    # def get_object(self):
    #     return self.request.user

    def get_object(self, queryset=None):
        obj = LookingFor.objects.get(user=self.request.user)
        return obj


class InterestUpdateView(LoginRequiredMixin, UpdateView):
    model = Interest
    form_class = InterestUpdateForm
    template_name = "profiles/interest_update_form.html"

    def get_success_url(self):
        return reverse("profiles:detail", kwargs={"username": self.request.user})

    # def get_object(self):
    #     return self.request.user

    def get_object(self, queryset=None):
        obj = Interest.objects.get(user=self.request.user)
        return obj


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = "profiles/profile_update_form.html"

    def get_success_url(self):
        if (
            self.request.user.profile.profile_type == "COUPLE_MF"
            or self.request.user.profile.profile_type == "COUPLE_MM"
            or self.request.user.profile.profile_type == "COUPLE_FF"
        ):
            return "/edit_2nd_person/"
        else:
            return reverse("profiles:detail", kwargs={"username": self.request.user})

    # def get_success_url(self):
    #     return reverse("/edit_2nd_person/")

    # def get_object(self):
    #     return self.request.user

    def get_object(self, queryset=None):
        obj = Profile.objects.get(user=self.request.user)
        return obj

    def form_valid(self, form):
        # kwargs = super().get_form_kwargs()
        location = OuterPostCode.objects.get(postcode=form.instance.outer_postcode)
        form.instance.lat = location.lat
        form.instance.lon = location.lon
        form.instance.loc = Point(float(location.lat), float(location.lon))
        return super().form_valid(form)


class SetProfileTypeView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = SetProfileTypeForm
    template_name = "profiles/profile_update_form.html"
    success_url = "/edit_profile/"

    def get_object(self):
        return self.request.user

    # def get_object(self, queryset=None):
    #     obj = Profile.objects.get(user=self.request.user)
    #     return obj


class Profile2ndPersonView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = Profile2ndPersonForm
    template_name = "profiles/profile_update_form.html"
    # success_url = reverse('profile:detail', user.username)

    def get_success_url(self):
        return reverse("profiles:detail", kwargs={"username": self.request.user})

    def get_object(self):
        return self.request.user

    def get_object(self, queryset=None):
        obj = Profile.objects.get(user=self.request.user)
        return obj


class Profile1stPersonView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = Profile1stPersonForm
    template_name = "profiles/profile_update_form.html"
    # success_url = reverse('profile:detail', user.username)

    def get_success_url(self):
        return reverse("profiles:detail", kwargs={"username": self.request.user})

    def get_object(self):
        return self.request.user

    def get_object(self, queryset=None):
        obj = Profile.objects.get(user=self.request.user)
        return obj


class CoverImageUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileCoverUpdateForm
    template_name = "profiles/cover_update_form.html"

    def get_success_url(self):
        return reverse("profiles:detail", kwargs={"username": self.request.user})

    def get_object(self):
        return self.request.user

    # def get_object(self, queryset=None):
    #     obj = Profile.objects.get(user=self.request.user)
    #     return obj


class AvatarImageUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileAvatarUpdateForm
    template_name = "profiles/avatar_update_form.html"
    success_url = "/pages/"

    def get_success_url(self):
        return reverse("profiles:detail", kwargs={"username": self.request.user})

    def get_object(self):
        return self.request.user

    # def get_object(self, queryset=None):
    #     obj = Profile.objects.get(user=self.request.user)
    #     return obj


class ProfileFeedView(LoginRequiredMixin, DetailView):
    http_method_names = ["get"]
    template_name = "profiles/feed.html"
    model = User
    context_object_name = "user"
    slug_field = "username"
    slug_url_kwarg = "username"

    target_user = id
    context = {"target_user": target_user}

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileFeedView, self).get_context_data(*args, **kwargs)
        context["posts"] = Post.objects.filter(
            author__username=self.kwargs["username"]
        ).order_by("-date")
        return context


class ProfileGalleryView(LoginRequiredMixin, DetailView):
    http_method_names = ["get"]
    template_name = "profiles/gallery.html"
    model = User
    context_object_name = "user"
    slug_field = "username"
    slug_url_kwarg = "username"

    target_user = id
    context = {"target_user": target_user}

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileGalleryView, self).get_context_data(*args, **kwargs)
        context["images"] = UserGallery.objects.filter(
            owner__username=self.kwargs["username"]
        )
        return context


class ProfileAddGalleryView(LoginRequiredMixin, CreateView):
    model = UserGallery
    form_class = ProfileGalleryCreateForm
    template_name = "profiles/gallery_create_form.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse("profiles:gallery", kwargs={"username": self.request.user})

    # def get_object(self, queryset=None):
    #     obj = Profile.objects.get(user=self.request.user)
    #     return obj


def follow(request, username):
    target_user = get_object_or_404(User, username=username)
    if request.method == "POST":
        if request.user != target_user:
            follow_relationship, created = Follow.objects.get_or_create(
                follower=request.user, following=target_user
            )
            if created:
                messages.success(request, "You are now following a new user")
            if not created:
                follow_relationship.delete()
                messages.warning(request, "You have stopped following a user")

    return redirect("profiles:detail", username=username)
