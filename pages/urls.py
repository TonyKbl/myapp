from django.urls import path

from . import views
from feed import views as feedviews

app_name = "pages"

urlpatterns = [
    path(
        "pages/<str:town>/<str:county>/<str:country>/",
        views.PageListView.as_view(),
        name="list",
    ),
    path("pages.html", views.PageListView.as_view(), name="list"),
    path("pages.html?ord=<str:ord>", views.PageListView.as_view(), name="list"),
    path("swingers-clubs.html", views.ClubPageListView.as_view(), name="clublist"),
    path(
        "swingers-clubs.html?ord=<str:ord>",
        views.ClubPageListView.as_view(),
        name="clublist",
    ),
    # path(
    #     "page/<str:page_type>/<slug:slug>/email.html",
    #     views.send_club_email(),
    #     name="page_feed",
    # ),
    path(
        "page/<str:page_type>/<slug:slug>/feed.html",
        views.PageFeedView.as_view(),
        name="page_feed",
    ),
    path(
        "page/<str:page_type>/<slug:slug>.html",
        views.ClubPageDetailView.as_view(),
        name="detail",
    ),
    # path("page/<str:page_type>/<slug:slug>/gallery.html", views.PageGalleryView.as_view(), name="gallery"),
    path(
        "page/<str:page_type>/<slug:slug>/events.html",
        views.PageEventsView.as_view(),
        name="page_events",
    ),
    path(
        "page/<str:page_type>/<slug:slug>/reviews.html",
        views.PageReviewsView.as_view(),
        name="page_reviews",
    ),
    path("claim_page/<int:pk>/", views.PageAddClaimView.as_view(), name="claim_page"),
    path("add_club.html", views.ClubPageCreateView.as_view(), name="add_club"),
    path("add_hotel.html", views.HotelPageCreateView.as_view(), name="add_hotel"),
    path(
        "edit_page/<int:pk>/<str:page_type>/<slug:slug>",
        views.ClubPageUpdateView.as_view(),
        name="edit_page",
    ),
    path(
        "new_page_post/<int:id>",
        feedviews.CreateNewPagePost.as_view(),
        name="new_page_post",
    ),
    path("add_review/<int:pk>", views.PageAddReviewView.as_view(), name="add_review"),
    path("<int:pk>/add_host.html", views.PageAddHostView.as_view(), name="add_host"),
    path("page_follow/<slug:slug>/", views.page_follow, name="page_follow"),
    # path("new_page_post/<int:pk>/<slug:slug>", feedviews.CreateNewPagePost.as_view(), name="add_page_post"),
    path(
        "page/update-cover/<str:page_type>/<slug:slug>.html",
        views.PageCoverUpdateView.as_view(),
        name="page_update_cover",
    ),
    path(
        "page/update-avatar/<str:page_type>/<slug:slug>.html",
        views.PageAvatarUpdateView.as_view(),
        name="page_update_avatar",
    ),
]
