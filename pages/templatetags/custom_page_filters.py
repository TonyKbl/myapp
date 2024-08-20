from django import template
from django.db.models import Avg, Count
from ..models import PageFollow, PageReviews

register = template.Library()

@register.filter
def is_following_page(user, target_page):
    return PageFollow.objects.filter(follower=user, following=target_page).exists()

@register.simple_tag
def avg_rating(target_page):
    # return PageReviews.objects.filter(page_name=target_page).values()[0]
    average = PageReviews.objects.filter(page_name=target_page).aggregate(Avg('rating'))
    if average['rating__avg'] == None:
        return 0
    else:
        print(average)
        return round(average['rating__avg'], 2)
    # return PageReviews.objects.aggregate(Avg('rating'))

@register.simple_tag
def review_count(target_page):
    # return PageReviews.objects.filter(page_name=target_page).values()[0]
    count = PageReviews.objects.filter(page_name=target_page).aggregate(Count('rating'))
    return count['rating__count']
    # return PageReviews.objects.aggregate(Avg('rating'))