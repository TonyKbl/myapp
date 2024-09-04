from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from sorl.thumbnail import ImageField
from pages.models import Page
from datetime import datetime
from django_resized import ResizedImageField




# Create your models here.
class Events(models.Model):
    today = datetime.now()
    today_path = today.strftime("%Y/%m/%d") ## this will create something like "2011/08/30"
    upload_dir = "profile_images/%Y/%m/%d"

    # organiser = models.ForeignKey( 
    #   settings.AUTH_USER_MODEL, 
    #   on_delete=models.CASCADE, related_name="organiser",
    #   )
    organiser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organiser')
    location = models.ForeignKey(
      Page,
      on_delete=models.CASCADE,
      related_name = "location"
    )

    title = models.CharField(max_length=250, blank=False, null=False)

    description = models.TextField(max_length=2048, blank=False, null=False)
    host_list = models.CharField(max_length=100, blank=True, null=True)    
    image = ResizedImageField(blank=True, null=True, size=[900, 900], quality=70, upload_to=upload_dir, max_length=200)
    private = models.BooleanField(default=0)
