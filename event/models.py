from django.db import models
from django.contrib.auth.models import User
from pages.models import Page, PageHost
from profiles.models import Profile
from datetime import datetime
from django_resized import ResizedImageField
import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible


@deconstructible
class PathAndRename(object):
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split(".")[-1]
        # set filename as random string
        filename = "{}.{}".format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)


# Create your models here.
class MasterEvent(models.Model):
    # print(upload_dir)
    event_type = models.CharField(max_length=50, null=True, blank=False)
    organiser = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="organiser"
    )
    title = models.CharField(max_length=250, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    ot_men = models.BooleanField(null=False, blank=True)
    ot_women = models.BooleanField(null=False, blank=True)
    ot_mfcouples = models.BooleanField(null=False, blank=True)
    ot_ffcouples = models.BooleanField(null=False, blank=True)
    ot_mmcouples = models.BooleanField(null=False, blank=True)
    ot_tvts = models.BooleanField(null=False, blank=True)
    private = models.BooleanField(null=False, blank=True)
    # host_list = models.ForeignKey(PageHost, on_delete=models.PROTECT, max_length=100, blank=True, null=True)
    # image = ResizedImageField(upload_to=upload_dir, blank=True, null=True, size=[900, 900], quality=70, max_length=200)

    def __str__(self):
        return self.title


class ClubEvent(MasterEvent):
    today = datetime.now()
    today_path = today.strftime(
        "%Y/%m/%d"
    )  ## this will create something like "2011/08/30"
    upload_dir = "event_images/" + today_path

    image = ResizedImageField(
        size=[600, 600],
        upload_to=PathAndRename(upload_dir),
        max_length=200,
        null=True,
        blank=True,
    )
    location = models.ForeignKey(
        Page, on_delete=models.CASCADE, related_name="location"
    )


class Social(MasterEvent):
    today = datetime.now()
    today_path = today.strftime(
        "%Y/%m/%d"
    )  ## this will create something like "2011/08/30"
    upload_dir = "event_images/" + today_path

    image = ResizedImageField(
        size=[600, 600],
        upload_to=PathAndRename(upload_dir),
        max_length=200,
        null=True,
        blank=True,
    )
    Location = models.CharField(max_length=255, null=True, blank=False)


class Festival(MasterEvent):
    today = datetime.now()
    today_path = today.strftime(
        "%Y/%m/%d"
    )  ## this will create something like "2011/08/30"
    upload_dir = "event_images/" + today_path

    image = ResizedImageField(
        size=[600, 600],
        upload_to=PathAndRename(upload_dir),
        max_length=200,
        null=True,
        blank=True,
    )
    Location = models.CharField(max_length=255, null=True, blank=False)


class PrivateParty(MasterEvent):
    today = datetime.now()
    today_path = today.strftime(
        "%Y/%m/%d"
    )  ## this will create something like "2011/08/30"
    upload_dir = "event_images/" + today_path

    image = ResizedImageField(
        size=[600, 600],
        upload_to=PathAndRename(upload_dir),
        max_length=200,
        null=True,
        blank=True,
    )
    Location = models.CharField(max_length=255, null=True, blank=False)


class Meet(MasterEvent):
    MEET_TYPE_CHOICES = [
        ("SOC", "Social"),
        ("CLUB", "Club Meet"),
        ("OURS", "Meet at ours"),
        ("YOURS", "Meet at yours"),
    ]
    meet_type = models.CharField(choices=MEET_TYPE_CHOICES)
    Location = models.CharField(max_length=255, null=True, blank=False)


class Event(models.Model):
    default_admission_fees = (
        "Couples - £\nSingle Males - £\nSingle Females - £\nTV/TS - £"
    )
    event = models.ForeignKey(
        MasterEvent, on_delete=models.CASCADE, related_name="master_event"
    )
    date = models.DateField(blank=False, null=True)
    start_time = models.TimeField(blank=False, null=True)
    end_time = models.TimeField(blank=False, null=True)
    admission_fees = models.TextField(
        blank=False, null=True, default=default_admission_fees
    )
    additional_info = models.TextField(blank=True, null=True)
    private = models.BooleanField(default=0)

    def __str__(self):
        return self.event.title


class EventHost(models.Model):
    host = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="event_host"
    )
    event = models.ForeignKey(
        MasterEvent, on_delete=models.CASCADE, related_name="host_for"
    )

    class Meta:
        unique_together = ("host", "event")

    def __str__(self):
        return self.host.display_name

    def profile(self):
        return self.host


# class EventReview(models.Model):
#     class EventRatings(models.IntegerChoices):
#         ONE = (1,)
#         TWO = (2,)
#         THREE = (3,)
#         FOUR = (4,)
#         FIVE = (5,)

#     author = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name="event_reviewer"
#     )
#     event_name = models.ForeignKey(
#         MasterEvent, on_delete=models.CASCADE, related_name="event_reviewed"
#     )
#     rating = models.IntegerField(choices=EventRatings.choices)
#     text = models.CharField(max_length=2048, null=True, blank=True)
#     date = models.DateField(auto_now_add="True")

#     def __int__(self):
#         return self.Avg("rating")


# @receiver(post_save, sender=MasterEvent)
# def create_event(sender, instance, created, **kwargs):
#     """Create event dates when a master event is created"""
#     if created:
#         EventDate.objects.create(event=instance)
