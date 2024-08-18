from django import template
from django.db.models import Avg
from ..models import PageFollow, PageReviews

register = template.Library()

@register.filter
def is_following_page(user, target_page):
    return PageFollow.objects.filter(follower=user, following=target_page).exists()

@register.simple_tag
def avg_rating(target_page):
    # return PageReviews.objects.filter(page_name=target_page).values()[0]
    average = PageReviews.objects.filter(page_name=target_page).aggregate(Avg('rating')).values()
    return average
    # return PageReviews.objects.aggregate(Avg('rating'))