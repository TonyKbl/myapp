from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("add_article.html", views.BlogCreateView.as_view(), name="add_article"), 
    # path("pages.html", views.PageListView.as_view(), name="list"),  
    # path("page/<str:page_type>/<slug:slug>.html", views.PageDetailView.as_view(), name="detail"),  
]