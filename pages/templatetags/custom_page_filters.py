from django import template
from ..models import PageFollow

register = template.Library()

@register.filter
def is_following_page(user, target_page):
    return PageFollow.objects.filter(follower=user, following=target_page).exists()