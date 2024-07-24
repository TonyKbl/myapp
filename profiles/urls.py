from django.urls import path

from . import views

app_name = "profiles"

urlpatterns = [
    path("edit_profile/", views.ProfileUpdateView.as_view(), name="edit_profile"),
    path("feed/<str:username>/", views.ProfileFeedView.as_view(), name="feed"),
    path("profile/<str:username>/", views.ProfileDetailView.as_view(), name="detail"),
    path("gallery/<str:username>/", views.ProfileGalleryView.as_view(), name="photos"),
    path("follow/<str:username>/", views.follow, name="follow"),
]
