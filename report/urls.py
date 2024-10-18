from django.urls import path
from . import views

app_name = "report"

urlpatterns = [
    path("reports.html", views.ReportListView.as_view(), name="reports"),
    ]