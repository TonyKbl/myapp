from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from django.conf import settings
from django_resized import ResizedImageField
from profiles.models import Profile
from pages.models import Page
from profanity.validators import validate_is_profane

# Create your models here.
class Post(models.Model):
  author = models.ForeignKey( 
    settings.AUTH_USER_MODEL, 
    on_delete=models.CASCADE, related_name="posts",
    )
  post_type = models.CharField(max_length=10)
  feature_name = models.CharField(max_length=100)    
  text = models.CharField(max_length=500, validators=[validate_is_profane])
  date = models.DateTimeField(auto_now=True)
  image = ResizedImageField(upload_to='feed_images', null=True, blank=True)
  slug = models.SlugField("username")
  likes = models.ManyToManyField(User, related_name='liked_posts', through='PostLike')

  def __str__(self):
    return self.text[0:100]
    
class PostLike(models.Model):
  user=models.ForeignKey(User, on_delete=models.CASCADE)
  post=models.ForeignKey(Post, on_delete=models.CASCADE)    
  date = models.DateTimeField(auto_now=True)
    
class PagePost(models.Model):   

  author = models.ForeignKey( 
    settings.AUTH_USER_MODEL, 
    on_delete=models.CASCADE, related_name="page_posts",
    )
  
  name = models.ForeignKey(
    Page,
    on_delete=models.CASCADE,
    related_name = "posts_name"
  )

  post_type = models.CharField(max_length = 10, null = True, blank = True)
  text = models.CharField(max_length=500, validators=[validate_is_profane])
  date = models.DateTimeField(auto_now=True)
  image = ResizedImageField(size = [500, None], upload_to='page_feed_images', null=True, blank=True)    
  slug = models.SlugField("name")
  likes = models.ManyToManyField(User, related_name='liked_page_posts', through='PagePostLike')

  def __str__(self):
    return self.text[0:100]
    
class PagePostLike(models.Model):
  user=models.ForeignKey(User, on_delete=models.CASCADE)
  page_post=models.ForeignKey(PagePost, on_delete=models.CASCADE)    
  date = models.DateTimeField(auto_now=True)
    