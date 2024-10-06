from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from django.conf import settings
from profiles.models import Profile
from place_area.models import Region
from django.urls import reverse
from django.template.defaultfilters import slugify
from profanity.validators import validate_is_profane
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

class Page(models.Model):
    def custom_user():
        return User.objects.get(username='admin')
   
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
    lat=models.FloatField(null=True, blank=True)
    lon=models.FloatField(null=True, blank=True)
    loc = models.PointField(null=True, blank=True, srid=4326)

    region = models.ForeignKey(Region, null=True, blank=False, on_delete=models.SET_NULL)

    description = models.TextField( null=False, blank=False, validators=[validate_is_profane])

    phone_number = models.CharField( max_length=10, null=True, blank=True)
    show_phone_button = models.BooleanField(default=1)
    email = models.EmailField(max_length=255)
    show_email_button = models.BooleanField(default=1)

    website = models.URLField( max_length=255, null=True, blank=True, validators=[validate_is_profane])
    facebook = models.URLField( max_length=255, null=True, blank=True, validators=[validate_is_profane])
    x_twitter = models.URLField( max_length=255, null=True, blank=True, validators=[validate_is_profane])
    insta = models.URLField( max_length=255, null=True, blank=True, validators=[validate_is_profane])
    tiktok = models.URLField( max_length=255, null=True, blank=True, validators=[validate_is_profane])
        
    slug = models.SlugField(default="", null=False, unique=True)
    page_created = models.DateField(auto_now_add=True)
    page_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.page_name
    
    def get_absolute_url(self):
        return reverse("page", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.page_name)

        
        return super().save(*args, **kwargs)

    
    
class PageFollow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='page_following')
    following = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='page_followers')
    date = models.DateTimeField(auto_now_add='True')

    class Meta:
        unique_together = ('follower', 'following')  

    def __str__(self):
        return self.follower.username

class PageHost(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='host')
    page_name = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='host_for')

    class Meta:
        unique_together = ('host', 'page_name')

    def __str__(self):
        return self.host.username

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
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True)
    reason = models.TextField(blank=False, verbose_name='Reason for your claim')

    def __str__(self):
        return self.page_claimed.page_name
    


@receiver(post_save, sender=ClaimPage)
def send_claim_email(sender, instance, **kwargs):
    # obj_id = instance._id


    message = """A claim has been made for - 
    
    Page - {pg_name}
    Claimant - {claimant}
    Email - {email}
    Phone - {phone}
    
    Message
    =======
    {message}

    """.format(
        pg_name = instance.page_claimed.page_name,
        claimant = instance.claimant,
        email = instance.email,
        phone = instance.phone,
        message = instance.reason
        )
    
    send_mail('New Page Claim', message, 'tonykbl@yahoo.co.uk', ['tonykbl@yahoo.co.uk'], fail_silently=False)
 