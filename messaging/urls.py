from django.urls import path
from . import views

app_name = "messaging"

urlpatterns = [
    path("messaging/", views.Messages.as_view(), name="messages"),
    ]