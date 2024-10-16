from django.urls import path

from . import views
from feed import views as feedviews

app_name = "pages"

urlpatterns = [
    path("pages/<str:town>/<str:county>/<str:country>/", views.PageListView.as_view(), name="list"), 
    path("pages.html", views.PageListView.as_view(), name="list"),
    path("pages.html?ord=<str:ord>", views.PageListView.as_view(), name="list"),
    path("page/<str:page_type>/<slug:slug>/feed.html", views.PageFeedView.as_view(), name="page_feed"),  
    path("page/<str:page_type>/<slug:slug>/about.html", views.PageDetailView.as_view(), name="detail"),
    # path("page/<str:page_type>/<slug:slug>/gallery.html", views.PageGalleryView.as_view(), name="gallery"),
    path("page/<str:page_type>/<slug:slug>/reviews.html", views.PageReviewsView.as_view(), name="page_reviews"),   
    path("claim_page/<int:pk>/", views.PageAddClaimView.as_view(), name="claim_page"),    
    path("add_page/", views.PageCreateView.as_view(), name="add_page"),
    path("edit_page/<int:pk>/<str:page_type>/<slug:slug>", views.PageUpdateView.as_view(), name="edit_page"),
    path("new_page_post/<int:id>", feedviews.CreateNewPagePost.as_view(), name="new_page_post"),
    path("add_review/<int:pk>", views.PageAddReviewView.as_view(), name="add_review"),
    path("add_host/<int:pk>/", views.PageAddHostView.as_view(), name="add_host"),
    path("page_follow/<slug:slug>/", views.page_follow, name="page_follow"),
    # path("new_page_post/<int:pk>/<slug:slug>", feedviews.CreateNewPagePost.as_view(), name="add_page_post"),
]