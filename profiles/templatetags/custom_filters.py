from django import template
from ..models import Follow

register = template.Library()

@register.filter
def is_following(user, target_user):
    print('User-', user)
    print('Target User-', target_user)
    return Follow.objects.filter(follower=user, following=target_user).exists()

@register.simple_tag(takes_context=True)
def followers_count(context):
    request = context.get("request")
    return "20"

@register.simple_tag(takes_context=True)
def following_count(context):
    request = context.get("request")
    return "30"