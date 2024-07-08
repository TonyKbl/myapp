"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from feed import urls as feed_urls
from pages import urls as pages_urls
from parties import urls as parties_urls
from profiles import urls as profiles_urls
from messaging import urls as messaging_urls
from django.conf import settings
from django.urls import re_path as url
from django.shortcuts import render

def custom_page_not_found_view(request, exception):
   return render(request, "404.html", {})

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(feed_urls, namespace="feed/")),
    path("", include(pages_urls, namespace="pages/")),
    path("", include(pages_urls, namespace="edit_page/")),
    path("", include(parties_urls, namespace="parties/")),
    path("", include(profiles_urls, namespace="profiles/")),
    path("", include(profiles_urls, namespace="edit_profile/")),
    path("", include(messaging_urls, namespace="messages/")),

    url("", include("allauth.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
