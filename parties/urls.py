from django.urls import path
from . import views

app_name = "parties"

urlpatterns = [
    path("events/", views.Parties.as_view(), name="events"),
    ]