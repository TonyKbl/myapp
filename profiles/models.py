from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from sorl.thumbnail import ImageField
from django_resized import ResizedImageField
from datetime import date
from django.utils import timezone

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

        # Height Option
    ft = [4, 5, 6,]
    inch = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


    SELECT = ""
    f4 = "meN"
    f41 = "Bisexual"
    f42 = "Bicurious"
    f43 = "Orally Bi"
    f45 = "Bi Playful"
    f46 = "Gay"
    LESBIAN = "Lesbian"
    HEIGHT_CHOICES = [
        (SELECT, "Select Sexuality"),
        (f4, "ME CHOICES"),
        (f41, "Bisexual"),
        (f42, "Bicuriuos"),
        (f43, "Orally Bi"),
        (f45, "Bi Playful"),
        (f46, "Gay"),
        (LESBIAN, "Lesbian"),
    ]
    
    cover_image = ResizedImageField(size=[600, 200], upload_to='profiles')

    image = ResizedImageField(size=[600, 600], upload_to='profiles')
    
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
    
    DOB = models.DateTimeField(null = False, blank = False)
    
    # Sexuality Option
    SELECT = ""
    STRAIGHT = "Straight"
    BISEXUAL = "Bisexual"
    BI_CURIOUS = "Bicurious"
    BI_ORALLY = "Orally Bi"
    BI_PLAYFUL = "Bi Playful"
    GAY = "Gay"
    LESBIAN = "Lesbian"
    SEXUALITY_CHOICES = [
        (SELECT, "Select Sexuality"),
        (STRAIGHT, "Straight"),
        (BISEXUAL, "Bisexual"),
        (BI_CURIOUS, "Bicuriuos"),
        (BI_ORALLY, "Orally Bi"),
        (BI_PLAYFUL, "Bi Playful"),
        (GAY, "Gay"),
        (LESBIAN, "Lesbian"),
    ]
    sexuality = models.CharField(
        max_length=10,
        choices=SEXUALITY_CHOICES,
        default=SELECT,
    )

    height = models.CharField(
        max_length=16,
        choices=HEIGHT_CHOICES,
        default=SELECT,
    )
    name2 = models.CharField(max_length=20, null=True, blank=True)
    DOB2 = models.DateTimeField(null=True, blank=False)

    sexuality2 = models.CharField(
        max_length=10,
        null = True,
        blank = True,
        choices=SEXUALITY_CHOICES,
        default=SELECT,
    )

    date_joined = models.DateTimeField(auto_now=True)
    last_activity = models.DateTimeField(null=True, blank=True)

    # Python3 code to calculate age in years


    @property
    def age(self):
        today = timezone.now().date()
        age = int(
            today.year
            - (self.DOB.year)
            - ((today.month, today.day) < (self.DOB.month, self.DOB.day))
        )
        return age 

    @property
    def age2(self):
        today = timezone.now().date()
        age2 = int(
            today.year
            - (self.DOB2.year)
            - ((today.month, today.day) < (self.DOB2.month, self.DOB2.day))
        )
        return age2
    
    def __str__(self):
        return self.user.username


