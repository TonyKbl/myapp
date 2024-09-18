from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from django.conf import settings
from profiles.models import Profile
from django.urls import reverse
from django.template.defaultfilters import slugify
from profanity.validators import validate_is_profane

class Page(models.Model):
    def custom_user():
        return User.objects.get(username='admin')


# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.ForeignKey(Author, on_delete=models.SET(custom_user))
    
    class PageTypes(models.TextChoices):
        SWINGERS_CLUB = "Swingers Club",
        GAY_SAUNA = "Gay Sauna",
        CINEMA = "Adult Cinema",
        ONLINE_SHOP = "Online Shop",

    user = models.ForeignKey(User, on_delete=models.SET(custom_user), related_name = "user")
        
    page_type = models.CharField(max_length = 15, choices = PageTypes.choices)

    page_name = models.CharField( max_length=50, null=False, blank=False, unique=True)

    cover_image = ResizedImageField(size=[600, 200], upload_to='page_covers', max_length=200, null=True, blank=True)

    image = ResizedImageField(size=[600, 600], upload_to='page_avatars', max_length=200, null=True, blank=True)

    address1 = models.CharField( max_length=50, null=False, blank=False, validators=[validate_is_profane])
    address2 = models.CharField( max_length=50, null=True, blank=True, validators=[validate_is_profane])
    town_city = models.CharField( max_length=50, null=False, blank=False, validators=[validate_is_profane])
    county = models.CharField( max_length=50, null=False, blank=False, validators=[validate_is_profane])
    post_code = models.CharField( max_length=10, null=False, blank=False, validators=[validate_is_profane])

    description = models.TextField( null=False, blank=False, validators=[validate_is_profane])

    phone_number = models.CharField( max_length=10, null=True, blank=True)

    website = models.CharField( max_length=255, null=True, blank=True, validators=[validate_is_profane])
    facebook = models.CharField( max_length=255, null=True, blank=True, validators=[validate_is_profane])
    x_twitter = models.CharField( max_length=255, null=True, blank=True, validators=[validate_is_profane])
    insta = models.CharField( max_length=255, null=True, blank=True, validators=[validate_is_profane])
    tiktok = models.CharField( max_length=255, null=True, blank=True, validators=[validate_is_profane])
        
    slug = models.SlugField(default="", null=False, unique=True)
    page_created = models.DateField(auto_now_add=True)
    page_updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("page", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.page_name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.page_name
    
class PageFollow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='page_following')
    following = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='page_followers')
    date = models.DateTimeField(auto_now_add='True')

    class Meta:
        unique_together = ('follower', 'following')

class PageReviews(models.Model):
    class PageRatings(models.IntegerChoices):
        ONE = 1,
        TWO = 2,
        THREE = 3,
        FOUR = 4,
        FIVE = 5,
    

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewer')
    page_name = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='reviewed_page')
    rating = models.IntegerField(choices=PageRatings.choices)
    text = models.CharField(max_length=2048)
    date = models.DateField(auto_now_add='True')

    def __int__(self):
        return self.Avg('rating')
    

class ClaimPage(models.Model):
    claimant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='claimant')
    page_claimed = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='claimed_page')
    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=255, blank=True)
    reason = models.TextField(blank=False, verbose_name='Reason for your claim')

    def __str__(self):
        return self.page_claimed.page_name
 