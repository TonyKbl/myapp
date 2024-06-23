from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from sorl.thumbnail import ImageField
from django_resized import ResizedImageField

@receiver(post_save, sender=User)   
def create_user_profile(sender, instance, created, **kwargs):
    """Create a new profile when a new user joins"""
    if created:
        Profile.objects.create(user=instance)

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
      User,
      on_delete=models.CASCADE,
      related_name = "profile"
    )
    
    image = ResizedImageField(size=[500, 500], upload_to='profiles')
    
    headline = models.CharField( max_length=200, null=True, blank=True)

    intro = models.CharField( max_length=200, null=True, blank=True)

    description = models.TextField()

    # profile type option
    SELECT = ""
    MALE = "SM"
    FEMALE = "SF"
    CD_TV = "CD/TV"
    TV_TS = "TV/TS"
    COUPLE_MF = "MF Couple"
    COUPLE_FF = "Couple FF"
    PROFILE_TYPE_CHOICES = [
        (SELECT, "Select Profile Type"),
        (MALE, "Single Male"),
        (FEMALE, "Single Female"),
        (CD_TV, "CD_TV"),
        (TV_TS, "TV_TS"),
        (COUPLE_MF, "Couple MF"),
        (COUPLE_FF, "Couple FF"),
    ]
    profile_type = models.CharField(
        max_length=10,
        choices=PROFILE_TYPE_CHOICES,
        default=SELECT,
    )

    location = models.CharField(max_length=25)
    
    name = models.CharField(max_length=20)
    # DOB = models.DateField(null = False, blank = False)
    
    # Sexuality Option
    SELECT = ""
    STRAIGHT = "ST"
    BISEXUAL = "BI"
    BI_CURIOUS = "BC"
    BI_ORALLY = "BO"
    BI_PLAYFUL = "BP"
    GAY = "G"
    LESBIAN = "L"
    SEXUALITY_CHOICES = [
        (SELECT, "Select Sexuality"),
        (STRAIGHT, "Straight"),
        (BISEXUAL, "Bisexial"),
        (BI_CURIOUS, "Bi Curious"),
        (BI_ORALLY, "Orally Bi"),
        (BI_PLAYFUL, "Playfully Bi"),
        (GAY, "Gay"),
        (LESBIAN, "Lesbian"),
    ]
    sexuality = models.CharField(
        max_length=2,
        choices=SEXUALITY_CHOICES,
        default=SELECT,
    )

    name2 = models.CharField(max_length=20, null=True, blank=True)
    # DOB2 = models.DateField(null=True, blank=False)

    sexuality2 = models.CharField(
        max_length=2,
        null = True,
        blank = True,
        choices=SEXUALITY_CHOICES,
        default=SELECT,
    )

    date_joined = models.DateTimeField(auto_now=True)
    last_activity = models.DateTimeField(null=True, blank=True)

    

    def __str__(self):
        return self.user.username


