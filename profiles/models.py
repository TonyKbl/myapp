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
        (f4, "4ft 0in"),
        (f41, "4ft 1in"),
        (f42, "4ft 2in"),
        (f43, "4ft 3in"),
        (f44, "4ft 4in"),
        (f45, "4ft 5in"),
        (f46, "4ft 6in"),
        (f47, "4ft 7in"),
        (f48, "4ft 8in"),
        (f49, "4ft 9in"),
        (f410, "4ft 10in"),
        (f411, "4ft 11in"),
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
        (f67, "6ft 7in"),
        (f68, "6ft 8in"),
        (f69, "6ft 9in"),
        (f610, "6ft 10in"),
        (f611, "6ft 11in"),
        (f70, "7ft 0in"),
    ]
    
    # body_type options

    SELECT = ""
    SLIM = "Slim"
    ATHLETIC = "Athletic"
    CURVY = "Curvy"
    DADBOD = "Dad Bod"
    LARGE = "Large"
    BODY_TYPE_CHOICES = [
        (SELECT, "Select Profile Type"),
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
        (VAPER, "Vape"),
    ]


    cover_image = ResizedImageField(size=[600, 200], upload_to='profiles')

    image = ResizedImageField(size=[100, 100], upload_to='profiles')

    display_name = models.CharField( max_length=50, null = True, blank = False )
    
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
    
    


