from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from sorl.thumbnail import ImageField
from pages.models import Page




# Create your models here.
class Parties(models.Model):
    organiser = models.OneToOneField(
      Page,
      on_delete=models.CASCADE,
      related_name = "party"
    )
    
    image = ImageField(upload_to='parties')