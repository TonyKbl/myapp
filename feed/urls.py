from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "feed"

urlpatterns = [
    path("", views.HomePage.as_view(), name="index"),
    path("home.html", views.Home.as_view(), name="index"),
    path(
        "post_detail/<str:page_type>/<int:pk>/",
        views.PostDetailView.as_view(),
        name="detail",
    ),
    path("new.html", views.CreateNewPost.as_view(), name="new_post"),
    # path("new_page_post/<int:id>", views.CreateNewPagePost.as_view(), name="new_page_post"),
    path(
        "about",
        TemplateView.as_view(template_name="feed/landing.html"),
        name="about",
    ),
]
