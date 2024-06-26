from django.urls import path

from . import views

app_name = "profiles"

urlpatterns = [
    path("profile/<str:username>/", views.ProfileDetailView.as_view(), name="detail"),
    path("edit_profile/", views.ProfileUpdateView.as_view(), name="edit_profile"),
]
