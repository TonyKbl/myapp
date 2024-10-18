from django.urls import path


from . import views

app_name = "profiles"

urlpatterns = [
    path("search_user.html", views.ProfileList.as_view(), name="search_user"),
    path("edit_profile/", views.ProfileUpdateView.as_view(), name="edit_profile"),
    path("edit_looking_for/", views.LookingForUpdateView.as_view(), name="edit_profile"),
    path("edit_interests/", views.InterestUpdateView.as_view(), name="edit_interests"),
    path("set_profile_type/", views.SetProfileTypeView.as_view(), name="set_profile_type"),
    path("edit_2nd_person/", views.Profile2ndPersonView.as_view(), name="edit_2nd_person"),
    path("feed/<str:username>/", views.ProfileFeedView.as_view(), name="feed"),
    path("profile/<str:username>/", views.ProfileDetailView.as_view(), name="detail"),
    path("follow/<str:username>/", views.follow, name="follow"),
    path("gallery/<str:username>/", views.ProfileGalleryView.as_view(), name="gallery"),
    path("gallery_upload/<str:username>/", views.ProfileAddGalleryView.as_view(), name="gallery_upload"),
    path("update_cover/", views.CoverImageUpdateView.as_view(), name="update_cover"),
    path("update_avatar/", views.AvatarImageUpdateView.as_view(), name="update_avatar"),
]
