from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from sorl.thumbnail import ImageField
from pages.models import Page, PageHost
from datetime import datetime
from django_resized import ResizedImageField



# Create your models here.
class Event(models.Model):
    today = datetime.now()
    today_path = today.strftime("%Y/%m/%d") ## this will create something like "2011/08/30"
    upload_dir = "event_images/%Y/%m/%d"

    organiser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organiser')
    location = models.ForeignKey(
      Page,
      on_delete=models.CASCADE,
      related_name = "location"
    )

    title = models.CharField(max_length=250, blank=False, null=False)

    description = models.TextField(blank=False, null=False)
    host_list = models.ManyToManyField(PageHost, max_length=100, blank=True)    
    image = ResizedImageField(blank=True, null=True, size=[900, 900], quality=70, upload_to=upload_dir, max_length=200)
       
    def __str__(self):
        return self.title 
    

class EventDate(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='master_event')
    date = models.DateField(blank=False, null=True)
    start_time = models.TimeField(blank=False, null=True)
    end_time = models.TimeField(blank=False, null=True)
    admission_fees = models.TextField(blank=False, null=True)
    additional_info = models.TextField(blank=True, null=True)
    private = models.BooleanField(default=0)

    def __str__(self):
        return self.event.title


class EventReview(models.Model):
    class EventRatings(models.IntegerChoices):
        ONE = 1,
        TWO = 2,
        THREE = 3,
        FOUR = 4,
        FIVE = 5,

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_reviewer')
    event_name = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_reviewed')
    rating = models.IntegerField(choices=EventRatings.choices)
    text = models.CharField(max_length=2048, null=True, blank=True)
    date = models.DateField(auto_now_add='True')

    def __int__(self):
        return self.Avg('rating')




# @receiver(post_save, sender=Event)   
# def create_event_dates(sender, instance, created, **kwargs):
#     """Create event dates when a master event is created"""
#     if created:
#         EventDate.objects.create(event=instance)