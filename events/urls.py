from django.urls import path
from . import views

app_name = "events"

urlpatterns = [
    path("events/", views.EventsList.as_view(), name="events"),
    path("add_event/<int:pk>", views.PageAddEventView.as_view(), name="add_event"),
    ]