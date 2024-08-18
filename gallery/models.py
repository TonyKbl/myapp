from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime

today = datetime.now()
today_path = today.strftime("%Y/%m/%d") ## this will create something like "2011/08/30"

# Create your models here.
class UserGallery(models.Model):
    today = datetime.now()
    today_path = today.strftime("%Y/%m/%d") ## this will create something like "2011/08/30"
    upload_dir = "profile_images/%Y/%m/%d"

    owner = models.ForeignKey( 
    settings.AUTH_USER_MODEL, 
    on_delete=models.CASCADE, related_name="owner",
    )
    image = models.ImageField(upload_to="profiles")
    private = models.BooleanField(default=0)


# class PageGallery(models.Model):
#     today = datetime.now()
#     today_path = today.strftime("%Y/%m/%d") ## this will create something like "2011/08/30"
#     upload_dir = "page_images/%Y/%m/%d"

#     owner = models.ForeignKey( 
#     settings.AUTH_USER_MODEL, 
#     on_delete=models.CASCADE, related_name="owner",
#     )
#     image = models.ImageField(upload_to=upload_dir)
#     private = models.BooleanField(default=0)