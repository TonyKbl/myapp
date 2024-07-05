from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from django.conf import settings
from profiles.models import Profile
from django.urls import reverse
from django.template.defaultfilters import slugify

class Page(models.Model):
    
    class PageTypes(models.TextChoices):
        SWINGERS_CLUB = "Swingers Club",
        GAY_SAUNA = "Gay Sauna",
        CINEMA = "Adult Cinema",
        ONLINE_SHOP = "Online Shop",

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "user")
        
    page_type = models.CharField(max_length = 15, choices = PageTypes.choices)

    page_name = models.CharField( max_length=50, null=False, blank=False)

    # owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name = "owner")

    cover_image = ResizedImageField(size=[600, 200], upload_to='profiles', null=True, blank=True)

    image = ResizedImageField(size=[600, 600], upload_to='profiles', null=True, blank=True)

    address1 = models.CharField( max_length=50, null=False, blank=False)
    address2 = models.CharField( max_length=50, null=True, blank=True)
    town_city = models.CharField( max_length=50, null=False, blank=False)
    county = models.CharField( max_length=50, null=False, blank=False)
    post_code = models.CharField( max_length=10, null=False, blank=False)

    description = models.TextField( null=False, blank=False)

    
    slug = models.SlugField(default="", null=False, unique=True)

    def get_absolute_url(self):
        return reverse("page", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.page_name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.page_name