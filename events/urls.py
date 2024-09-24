from django.urls import path
from . import views

app_name = "events"

urlpatterns = [
    path("events.html", views.EventsList.as_view(), name="events"),
    path("events/<int:pk>", views.PageEventsList.as_view(), name="page_events"),
    path("add_event/<int:pk>", views.PageAddEventView.as_view(), name="add_event"),
    path("add_date/<int:pk>", views.AddEventDateView.as_view(), name="add_date"),
    path("swinger-club-event/<int:pk>/<str:club>/<str:date>/<str:title>.html", views.EventDetailView.as_view(), name="event_detail"),  
    ]