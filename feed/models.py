from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from django.conf import settings
from django_resized import ResizedImageField
from profiles.models import Profile

# Create your models here.
class Post(models.Model):
    # author = models.ForeignKey(
    #   User,
    #   on_delete=models.CASCADE,
    #   related_name = "posts"
    # )
    author = models.ForeignKey( 
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, related_name="posts",
        )
    feature_type = models.CharField(max_length=10)
    feature_name = models.CharField(max_length=100)    
    text = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now=True)
    image = ResizedImageField(upload_to='feed_images', null=True, blank=True)
    slug = models.SlugField("username")

    def __str__(self):
      return self.text[0:100]
    
# class PagePost(models.Model):
#     # author = models.ForeignKey(
#     #   User,
#     #   on_delete=models.CASCADE,
#     #   related_name = "posts"
#     #)
#     author = models.ForeignKey( 
#         settings.AUTH_USER_MODEL, 
#         on_delete=models.CASCADE, related_name="pageposts",
#         )
#     feature_type = models.CharField(max_length=10)
#     feature_name = models.CharField(max_length=100)    
#     text = models.CharField(max_length=300)
#     date = models.DateTimeField(auto_now=True)
#     image = ResizedImageField(upload_to='feed_images', null=True, blank=True)
    