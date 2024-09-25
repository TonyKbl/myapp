from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from django.conf import settings
from django.template.defaultfilters import slugify
from profanity.validators import validate_is_profane
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

# Create your models here.

class Tags(models.Model):
    tag = models.CharField(max_length=30)

    def __str__(self):
        return self.tag

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    title = models.CharField(max_length=255, blank=False, null=False)
    article = models.TextField(blank=False, null=False)
    tags = models.ManyToManyField(Tags, blank=True)

    def __str__(self):
        return self.title

