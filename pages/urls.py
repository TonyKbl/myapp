from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path("pages/<str:town>/<str:county>/<str:country>/", views.PageListView.as_view(), name="list"), 
    path("pages/", views.PageListView.as_view(), name="list"),  
    path("page/<slug:slug>/", views.PageDetailView.as_view(), name="detail"),    
    path("add_page/", views.PageCreateView.as_view(), name="add_page"),
    path("edit_page/", views.PageUpdateView.as_view(), name="edit_page"),
]