from django.urls import path
from . import views

app_name = "messaging"

urlpatterns = [
    path("inbox.html", views.MessageInboxView.as_view(), name="messages"),
    path("messages/<int:pk>", views.MessageView.as_view(), name="message"),
    path("send/<int:pk>", views.SendMessageView.as_view(), name="send"),
    ]