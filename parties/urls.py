from django.urls import path
from . import views

app_name = "parties"

urlpatterns = [
    path("meets/", views.Parties.as_view(), name="meets"),
    ]