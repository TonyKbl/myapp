from django.urls import path

from . import views

app_name = "search"

urlpatterns = [
    path("search.html", views.SearchAll.as_view(), name="search"), 
]