from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_resized import ResizedImageField

from profanity.validators import validate_is_profane
# from sorl.thumbnail import ImageField


# Create your models here.
class Message(models.Model):
    msg_from = models.ForeignKey(
      User,
      on_delete=models.CASCADE,
      related_name = "msg_from"
    )

    msg_to = models.ForeignKey(
      User,
      on_delete=models.CASCADE,
      related_name = "msg_to"
    )
    message = models.TextField(blank=True, null=True, validators=[validate_is_profane])
    date_sent = models.DateField(auto_now=True)
    date_read = models.DateField(auto_now=True)
    time_sent = models.TimeField(auto_now=True)
    time_read = models.TimeField(auto_now=True)
    read = models.BooleanField(null=True)
    
    attachment = ResizedImageField(size=[600, 600], upload_to='message_attachments', blank=True, null=True)