from django import template
from ..models import PageReviews

register = template.Library()

@register.simple_tag
def avg_ratings():
    return PageReviews.objects.all().avg()

