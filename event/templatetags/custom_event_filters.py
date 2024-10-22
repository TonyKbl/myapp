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
