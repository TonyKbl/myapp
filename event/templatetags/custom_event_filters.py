from django import template
from django.db.models import Avg, Count
from ..models import Guestlist
from django.http import HttpResponse, request
from urllib.parse import urlencode

register = template.Library()


@register.filter
def is_on_guestlist(target_user, target_event):
    print(target_user, target_event)
    gl_id = Guestlist.objects.filter(guest=target_user, event=target_event)
    return gl_id


@register.simple_tag
def guestlist_count(target_event):
    # good query
    # count = Guestlist.objects.filter(event=target_event).aggregate(Count("guest"))
    count = Guestlist.objects.filter(event=target_event, profile_type="Man").aggregate(
        Count("guest")
    )
    # count = guests.objects.filter
    return count["guest__count"]


@register.simple_tag
def guestlist_man_count(target_event):
    # good query
    # count = Guestlist.objects.filter(event=target_event).aggregate(Count("guest"))
    count = Guestlist.objects.filter(event=target_event, profile_type="Man").aggregate(
        Count("guest")
    )
    # count = guests.objects.filter
    return count["guest__count"]


@register.simple_tag
def guestlist_woman_count(target_event):
    # good query
    # count = Guestlist.objects.filter(event=target_event).aggregate(Count("guest"))
    count = Guestlist.objects.filter(
        event=target_event, profile_type="Woman"
    ).aggregate(Count("guest"))
    # count = guests.objects.filter
    return count["guest__count"]


@register.simple_tag
def guestlist_couple_count(target_event):
    # good query
    # count = Guestlist.objects.filter(event=target_event).aggregate(Count("guest"))
    count = Guestlist.objects.filter(
        event=target_event, profile_type="MF Couple"
    ).aggregate(Count("guest"))
    # count = guests.objects.filter
    return count["guest__count"]


@register.simple_tag
def guestlist_trans_count(target_event):
    # good query
    # count = Guestlist.objects.filter(event=target_event).aggregate(Count("guest"))
    count = Guestlist.objects.filter(event=target_event, profile_type="Man").aggregate(
        Count("guest")
    )
    # count = guests.objects.filter
    return count["guest__count"]
