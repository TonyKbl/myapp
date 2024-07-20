from django.urls import path
from . import views

app_name = "feed"

urlpatterns = [
    path("", views.HomePage.as_view(), name="index"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("new.html", views.CreateNewPost.as_view(), name="new_post"),
    # path("new_page_post/<int:id>", views.CreateNewPagePost.as_view(), name="new_page_post"),
]
