from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from sorl.thumbnail import ImageField


# Create your models here.
class Parties(models.Model):
    user = models.OneToOneField(
      User,
      on_delete=models.CASCADE,
      related_name = "parties"
    )
    
    image = ImageField(upload_to='parties')