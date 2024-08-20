from django import template
from django.db.models import Avg, Count
from ..models import PageFollow, PageReviews
from django.http import HttpResponse

register = template.Library()

@register.filter
def is_following_page(user, target_page):
    return PageFollow.objects.filter(follower=user, following=target_page).exists()

@register.simple_tag
def avg_rating(target_page):
    # return PageReviews.objects.filter(page_name=target_page).values()[0]
    average = PageReviews.objects.filter(page_name=target_page).aggregate(Avg('rating'))
    if average['rating__avg'] == None:
        return '<i style = "color:gray;" class="bi bi-star"></i><i style = "color:gray;" class="bi bi-star"></i><i style = "color:gray;" class="bi bi-star"></i><i style = "color:gray;" class="bi bi-star"></i><i style = "color:gray;" class="bi bi-star"></i>'
    elif average['rating__avg'] <= 1.5:
        return '<i style = "color:yellow;" class="bi bi-star-fill"></i><i style = "color:gray;" class="bi bi-star"></i><i style = "color:gray;" class="bi bi-star"></i><i style = "color:gray;" class="bi bi-star"></i><i style = "color:gray;" class="bi bi-star"></i>'
    elif 1.5 <= average['rating__avg'] <= 2.5:
        return '<i style = "color:yellow;" class="bi bi-star-fill"></i><i style = "color:yellow;" class="bi bi-star-fill"></i><i style = "color:gray;" class="bi bi-star"></i><i style = "color:gray;" class="bi bi-star"></i><i style = "color:gray;" class="bi bi-star"></i>'
    elif 2.5 <= average['rating__avg'] <= 3.5:
        return '<i style = "color:yellow;" class="bi bi-star-fill"></i><i style = "color:yellow;" class="bi bi-star-fill"></i><i style = "color:yellow;" class="bi bi-star-fill"></i><i style = "color:gray;" class="bi bi-star"></i><i style = "color:gray;" class="bi bi-star"></i>'
    elif 3.5 <= average['rating__avg'] <= 4.5:
        return '<i style = "color:yellow;" class="bi bi-star-fill"></i><i style = "color:yellow;" class="bi bi-star-fill"></i><i style = "color:yellow;" class="bi bi-star-fill"></i><i style = "color:yellow;" class="bi bi-star-fill"></i><i style = "color:gray;" class="bi bi-star"></i>'
    elif 4.5 <= average['rating__avg'] <= 5:
        return '<i style = "color:yellow;" class="bi bi-star-fill"></i><i style = "color:yellow;" class="bi bi-star-fill"></i><i style = "color:yellow;" class="bi bi-star-fill"></i><i style = "color:yellow;" class="bi bi-star-fill"></i><i style = "color:yellow;" class="bi bi-star-fill"></i>'
        
    else:        
        return round(average['rating__avg'], 2)
    # return PageReviews.objects.aggregate(Avg('rating'))

@register.simple_tag
def review_count(target_page):
    # return PageReviews.objects.filter(page_name=target_page).values()[0]
    count = PageReviews.objects.filter(page_name=target_page).aggregate(Count('rating'))
    return count['rating__count']
    # return PageReviews.objects.aggregate(Avg('rating'))