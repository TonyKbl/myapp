from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_resized import ResizedImageField
# from sorl.thumbnail import ImageField


# Create your models here.
class Message(models.Model):
    msg_from = models.OneToOneField(
      User,
      on_delete=models.CASCADE,
      related_name = "msg_from"
    )

    msg_to = models.OneToOneField(
      User,
      on_delete=models.CASCADE,
      related_name = "msg_to"
    )
    message = models.TextField(blank=True, null=True)
    date_sent = models.DateTimeField(auto_now=True)
    date_read = models.DateTimeField(auto_now=True)
    read = models.BooleanField()
    
    attachment = ResizedImageField(size=[600, 200], upload_to='message_attachments', blank=True, null=True)