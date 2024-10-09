from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from sorl.thumbnail import ImageField
from django_resized import ResizedImageField
from datetime import date
from django.utils import timezone
from django.conf import settings
from profanity.validators import validate_is_profane
from place_area.models import OuterPostCode
import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible


@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # set filename as random string
        filename = '{}-{}.{}'.format(instance.pk, uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)
 

@receiver(post_save, sender=User)   
def create_user_profile(sender, instance, created, **kwargs):
    """Create a new profile when a new user joins"""
    if created:
        Profile.objects.create(user=instance)
        UserLevel.objects.create(user=instance)
        LookingFor.objects.create(user=instance)
        

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
      User,
      on_delete=models.CASCADE,
      related_name = "profile"
    )


        # Height Option

    SELECT = ""
    f4 = "4ft 0in"
    f41 = "4ft 1in"
    f42 = "4ft 2in"
    f43 = "4ft 3in"
    f44 = "4ft 4in"
    f45 = "4ft 5in"
    f46 = "4ft 6in"
    f47 = "4ft 7in"
    f48 = "4ft 8in"
    f49 = "4ft 9in"
    f410 = "4ft 10in"
    f411 = "4ft 11in"
    f50 = "5ft 0in"
    f51 = "5ft 1in"
    f52 = "5ft 2in"
    f53 = "5ft 3in"
    f54 = "5ft 4in"
    f55 = "5ft 5in"
    f56 = "5ft 6in"
    f57 = "5ft 7in"
    f58 = "5ft 8in"
    f59 = "5ft 9in"
    f510 = "5ft 10in"
    f511 = "5ft 11in"
    f60 = "6ft 0in"
    f61 = "6ft 1in"
    f62 = "6ft 2in"
    f63 = "6ft 3in"
    f64 = "6ft 4in"
    f65 = "6ft 5in"
    f66 = "6ft 6in"
    f67 = "6ft 7in"
    f68 = "6ft 8in"
    f69 = "6ft 9in"
    f610 = "6ft 10in"
    f611 = "6ft 11in"
    f70 = "7ft 0in"
    HEIGHT_CHOICES = [
        (SELECT, "Select Height"),
        (f411, "<5ft"),
        (f50, "5ft 0in"),
        (f51, "5ft 1in"),
        (f52, "5ft 2in"),
        (f53, "5ft 3in"),
        (f54, "5ft 4in"),
        (f55, "5ft 5in"),
        (f56, "5ft 6in"),
        (f57, "5ft 7in"),
        (f58, "5ft 8in"),
        (f59, "5ft 9in"),
        (f510, "5ft 10in"),
        (f511, "5ft 11in"),
        (f60, "6ft 0in"),
        (f61, "6ft 1in"),
        (f62, "6ft 2in"),
        (f63, "6ft 3in"),
        (f64, "6ft 4in"),
        (f65, "6ft 5in"),
        (f66, "6ft 6in"),
        (f67, ">6ft 6in"),
    ]
    
    # body_type options

    SELECT = ""
    SLIM = "Slim"
    ATHLETIC = "Athletic"
    CURVY = "Curvy"
    DADBOD = "Dad Bod"
    LARGE = "Large"
    BODY_TYPE_CHOICES = [
        (SELECT, "Select Body Type"),
        (SLIM, "Slim"),
        (ATHLETIC, "Athletic"),
        (CURVY, "Curvy"),
        (DADBOD, "Dad Bod"),
        (LARGE, "Large"),
    ]

    # Smoke Options
    SELECT = ""
    NEVER = "Never"
    OCCASIONALLY = "Occasionally"
    SOCIALLY = "Socially"
    OFTEN = "Often"
    VAPER = "Vape"
    SMOKER_TYPE_CHOICES = [
        (SELECT, "Select Smoker Type"),
        (NEVER, "Never"),
        (OCCASIONALLY, "Occasionally"),
        (SOCIALLY, "Socially"),
        (OFTEN, "Often"),
        (VAPER, "Vape"),
    ]

        # Drink Options
    SELECT = ""
    NEVER = "Never"
    OCCASIONALLY = "Occasionally"
    SOCIALLY = "Socially"
    OFTEN = "Often"
    DRINK_TYPE_CHOICES = [
        (SELECT, "Select Option"),
        (NEVER, "Never"),
        (OCCASIONALLY, "Occasionally"),
        (SOCIALLY, "Socially"),
        (OFTEN, "Often"),
    ]


    cover_image = ResizedImageField(size=[600, 200], upload_to=PathAndRename('profile/cover'), max_length=200)

    image = ResizedImageField(size=[100, 100], upload_to=PathAndRename('profile/avatar'), max_length=200)

    display_name = models.CharField( max_length=50, null = True, blank = False )
    
    status = models.CharField( max_length=200, null=True, blank=True, validators=[validate_is_profane])

    intro = models.CharField( max_length=200, null=True, blank=True, validators=[validate_is_profane])

    description = models.TextField(null=True, validators=[validate_is_profane])

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
    # outer_postcode = models.CharField(max_length=10, null=True, blank=False)
    outer_postcode = models.ForeignKey(OuterPostCode, on_delete=models.CASCADE, blank=False, null=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    loc = models.PointField(null=True, blank=True)

    
    name = models.CharField(max_length=20)
    
    DOB = models.DateTimeField(null = True, blank = False)
    
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

    body_type = models.CharField(
        max_length=16,
        choices=BODY_TYPE_CHOICES,
        default=SELECT,
    )

    smoke = models.CharField(
        max_length=16,
        choices=SMOKER_TYPE_CHOICES,
        default=SELECT,
    )

    drink = models.CharField(
        max_length=16,
        choices=DRINK_TYPE_CHOICES,
        default=SELECT,
    )


    name2 = models.CharField(max_length=20, null=True, blank=True)
    DOB2 = models.DateTimeField(null=True, blank=True)

    sexuality2 = models.CharField(
        max_length=10,
        null = True,
        blank = True,
        choices=SEXUALITY_CHOICES,
        default=SELECT,
    )

    height2 = models.CharField(
        max_length=16,
        choices=HEIGHT_CHOICES,
        default=SELECT,
        null = True,
        blank = True,
    )

    body_type2 = models.CharField(
        max_length=16,
        choices=BODY_TYPE_CHOICES,
        default=SELECT,
        null = True,
        blank = True,
    )

    smoke2 = models.CharField(
        max_length=16,
        choices=SMOKER_TYPE_CHOICES,
        default=SELECT,
        null = True,
        blank = True,
    )

    drink2 = models.CharField(
        max_length=16,
        choices=DRINK_TYPE_CHOICES,
        default=SELECT,
        null = True,
        blank = True,
    )


    date_joined = models.DateTimeField(auto_now_add=True)

    last_updated = models.DateTimeField(auto_now=True)

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
        if self.DOB2:
            today = timezone.now().date()
            age2 = int(
                today.year
                - (self.DOB2.year)
                - ((today.month, today.day) < (self.DOB2.month, self.DOB2.day))
            )
        else:
            age2 = 0
        return age2
    


    def __str__(self):
        return self.user.username    
    



class Level(models.Model):
    level = models.IntegerField(null=True, blank=False)
    level_name = models.CharField(max_length=50, null=True, blank=False)

    def __str__(self):
        return self.level_name
    

class UserLevel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='level')
    level = models.OneToOneField(Level, on_delete=models.DO_NOTHING, null=False, blank=False, default=10)

    def __str__(self):
        return self.user.username


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    date = models.DateTimeField(auto_now_add='True')

    class Meta:
        unique_together = ('follower', 'following')

    
class LookingFor(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    age_min = models.IntegerField(null=False, blank=False, default=18)
    age_max = models.IntegerField(null=False, blank=False, default=99)
    men = models.BooleanField(null=False, blank=False)
    women = models.BooleanField(null=False, blank=False, default=1)
    mf_couple = models.BooleanField(null=False, blank=False, default=1)
    ff_couple = models.BooleanField(null=False, blank=False, default=1)
    cd_tv = models.BooleanField(null=False, blank=False)
    tg_ts = models.BooleanField(null=False, blank=False)
    smokers = models.BooleanField(null=False, blank=False)
    can_travel = models.BooleanField(null=False, blank=False)
    can_accom = models.BooleanField(null=False, blank=False)

    def __str__(self):
        return self.user.username
    

class BlockedList(models.Model):
    blocker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blocker')
    blocked =models.ForeignKey(User, on_delete=models.CASCADE, related_name='blocked')

    class Meta:
        unique_together = ('blocker', 'blocked')

    def __str__(self):
        return self.blocker.username


