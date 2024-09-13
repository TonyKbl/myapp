from django.urls import path
from . import views

app_name = "messaging"

urlpatterns = [
    path("inbox.html", views.MessageInboxView.as_view(), name="messages"),
    ]