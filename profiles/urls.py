from django.urls import path


from . import views

app_name = "profiles"

urlpatterns = [
    path("edit_profile/", views.ProfileUpdateView.as_view(), name="edit_profile"),
    path("feed/<str:username>/", views.ProfileFeedView.as_view(), name="feed"),
    path("profile/<str:username>/", views.ProfileDetailView.as_view(), name="detail"),
    path("follow/<str:username>/", views.follow, name="follow"),
    path("gallery/<str:username>/", views.ProfileGalleryView.as_view(), name="photos"),
    path("gallery/upload/<str:username>/", views.follow, name="gallery_upload"),
    path("update_cover/", views.CoverImageUpdateView.as_view(), name="update_cover"),
    path("update_avatar/", views.AvatarImageUpdateView.as_view(), name="update_avatar"),
]
