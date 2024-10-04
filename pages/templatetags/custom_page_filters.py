from django import template
from django.db.models import Avg, Count
from ..models import PageFollow, PageReviews, PageHost
from django.http import HttpResponse, request
from urllib.parse import urlencode

register = template.Library()


@register.filter
def is_page_host(target_user, target_page):
    return PageHost.objects.filter(host=target_user, page_name=target_page).exists()


@register.filter
def is_following_page(user, target_page):
    return PageFollow.objects.filter(follower=user, following=target_page).exists()

@register.simple_tag
def avg_stars(target_page):
    # return PageReviews.objects.filter(page_name=target_page).values()[0]
    average = PageReviews.objects.filter(page_name=target_page).aggregate(Avg('rating'))
    if average['rating__avg'] == None:
        return '<i style = "color:gray;" class="bi bi-star"></i><i style = "color:gray;" class="bi bi-star"></i><i style = "color:gray;" class="bi bi-star"></i><i style = "color:gray;" class="bi bi-star"></i><i style = "color:gray;" class="bi bi-star"></i>'
    elif average['rating__avg'] <= 1.5:
        return '<i class="bi bi-star-fill text-warning"></i><i style = "color:gray;" class="bi bi-star"></i><i style = "color:gray;" class="bi bi-star"></i><i style = "color:gray;" class="bi bi-star"></i><i style = "color:gray;" class="bi bi-star"></i>'
    elif 1.5 <= average['rating__avg'] <= 2.5:
        return '<i class="bi bi-star-fill text-warning"></i><i class="bi bi-star-fill text-warning"></i><i style = "color:gray;" class="bi bi-star"></i><i style = "color:gray;" class="bi bi-star"></i><i style = "color:gray;" class="bi bi-star"></i>'
    elif 2.5 <= average['rating__avg'] <= 3.5:
        return '<i class="bi bi-star-fill text-warning"></i><i class="bi bi-star-fill text-warning"></i><i class="bi bi-star-fill text-warning"></i><i style = "color:gray;" class="bi bi-star"></i><i style = "color:gray;" class="bi bi-star"></i>'
    elif 3.5 <= average['rating__avg'] <= 4.5:
        return '<i class="bi bi-star-fill text-warning"></i><i class="bi bi-star-fill text-warning"></i><i class="bi bi-star-fill text-warning"></i><i class="bi bi-star-fill text-warning"></i><i style = "color:gray;" class="bi bi-star"></i>'
    elif 4.5 <= average['rating__avg'] <= 5:
        return '<i class="bi bi-star-fill text-warning"></i><i class="bi bi-star-fill text-warning"></i><i class="bi bi-star-fill text-warning"></i><i class="bi bi-star-fill text-warning"></i><i class="bi bi-star-fill text-warning"></i>'
        
    else:        
        return 0
    # return PageReviews.objects.aggregate(Avg('rating'))

@register.simple_tag
def avg_rating(target_page):
    # return PageReviews.objects.filter(page_name=target_page).values()[0]
    average = PageReviews.objects.filter(page_name=target_page).aggregate(Avg('rating'))
    print(average['rating__avg'])
    if average['rating__avg'] != None:
        return round(average['rating__avg'], 1)
    else:
        return 0.0

@register.simple_tag
def review_count(target_page):
    # return PageReviews.objects.filter(page_name=target_page).values()[0]
    count = PageReviews.objects.filter(page_name=target_page).aggregate(Count('rating'))
    return count['rating__count']
    # return PageReviews.objects.aggregate(Avg('rating'))

