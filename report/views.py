from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Report
# Create your views here.

class ReportListView(ListView):    
    http_method_names = ["get"]
    template_name = "pages/list.html"
    model = Report
    context_object_name = "report"