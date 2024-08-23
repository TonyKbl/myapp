from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from sorl.thumbnail import ImageField
from pages.models import Page




# Create your models here.
class Events(models.Model):
    organiser = models.ForeignKey(
      Page,
      on_delete=models.CASCADE,
      related_name = "events"
    )
    host_list = models.CharField(max_length=100)
    
    image = ImageField(upload_to='events')