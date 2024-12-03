from django.urls import path
from . import views

app_name = "events"

urlpatterns = [
    path("swinger-events.html", views.EventList.as_view(), name="events"),
    path("swinger-club-events.html", views.EventList.as_view(), name="club-events"),
    path("swinger-social-events.html", views.EventList.as_view(), name="social-events"),
    path(
        "adult-cinema-events.html",
        views.EventList.as_view(),
        name="adult-cinema-events",
    ),
    path("swinger-festivals.html", views.EventList.as_view(), name="swinger-festivals"),
    #     path("events/<int:pk>", views.PageEventsList.as_view(), name="page_events"),
    path(
        "add-club-event/<int:pk>/<str:page_name>.html",
        views.ClubAddEventView.as_view(),
        name="add_event",
    ),
    #     path("add-date/<int:pk>", views.AddEventDateView.as_view(), name="add_date"),
    path(
        "swingers-club-event/<int:pk>/<str:club>/<str:date>/<str:title>.html",
        views.EventDetailView.as_view(),
        name="event_detail",
    ),
    path(
        "join-guestlist/<int:pk>",
        views.ClubAddGuestlistView.as_view(),
        name="guestlist",
    ),
    path(
        "add-non-member/<int:pk>/<str:event>.html",
        views.ClubAddNonMemberGuestlistView.as_view(),
        name="non-member-guestlist",
    ),
    path(
        "remove-from-guestlist/<int:pk>",
        views.ClubDeleteGuestlistView.as_view(),
        name="guestlist",
    ),
    path(
        "master-events/<int:pk>/<str:club>.html",
        views.PageEventsList.as_view(),
        name="page_events",
    ),
    path(
        "guestlist/<int:pk>/<str:event>.html",
        views.GuestlistView.as_view(),
        name="view-guestlist",
    ),
    path(
        "add_date/<int:pk>/<slug:location>.html",
        views.AddEventDateView.as_view(),
        name="add_date",
    ),
    # Swinger Private Meets
    path("list-meets.html", views.PrivateMeetListView.as_view(), name="list-meets"),
    path("add-meet.html", views.PrivateMeetAddView.as_view(), name="add_meet"),
]
