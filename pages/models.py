from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from profiles.models import Profile

# Create your models here.
class Page(models.Model):
    user = models.OneToOneField(
      Profile,
      on_delete=models.CASCADE,
      related_name = "page"
    )

    cover_image = ResizedImageField(size=[600, 200], upload_to='profiles')

    image = ResizedImageField(size=[600, 600], upload_to='profiles')

    page_name = models.CharField( max_length=50, null=False, blank=False)

    intro = models.CharField( max_length=200, null=False, blank=False)

    description = models.TextField( null=False, blank=False)