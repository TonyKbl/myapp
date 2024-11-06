from django import template
from django.db.models import Avg, Count
from ..models import Guestlist, MasterEvent, Event
from django.http import HttpResponse, request
from urllib.parse import urlencode

register = template.Library()


@register.filter
def is_on_guestlist(target_user, target_event):
    gl_id = Guestlist.objects.filter(guest=target_user, event=target_event)
    return gl_id


@register.filter
def can_attend(target_profile_type, target_event):
    gl = MasterEvent.objects.get(id=target_event)
    if target_profile_type == "Man" and gl.ot_men:
        return True
    if target_profile_type == "Woman" and gl.ot_women:
        return True
    if target_profile_type == "Couple MF" and gl.ot_mfcouples:
        return True
    if target_profile_type == "Couple FF" and gl.ot_ffcouples:
        return True
    if target_profile_type == "Couple MM" and gl.ot_mmcouples:
        return True
    if target_profile_type == "CD/TV" and gl.ot_tvts:
        return True
    if target_profile_type == "TG/TS" and gl.ot_tvts:
        return True

    return False


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
        event=target_event, profile_type="Couple MF"
    ).aggregate(Count("guest"))
    # count = guests.objects.filter
    return count["guest__count"]


@register.simple_tag
def guestlist_trans_count(target_event):
    # good query
    # count = Guestlist.objects.filter(event=target_event).aggregate(Count("guest"))
    count_cd = Guestlist.objects.filter(
        event=target_event, profile_type="CD_TV"
    ).aggregate(Count("guest"))
    count_ts = Guestlist.objects.filter(
        event=target_event, profile_type="TG_TS"
    ).aggregate(Count("guest"))
    count = count_cd["guest__count"] + count_ts["guest__count"]
    return count
