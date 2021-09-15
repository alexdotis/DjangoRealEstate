from django import template
from django.db.models import Avg
from listing.models import Listing, ListingReview
from django.utils.safestring import mark_safe
register = template.Library()


@register.filter
def average_review(listing_title):
    pr = ListingReview.objects.filter(listing__title=listing_title)
    if pr.exists():
        return pr.values('listing__title').annotate(Avg('review'))[0]['review__avg']
    else:
        return 0


@register.simple_tag()
def rating(value):
    fullstar = '<i class="mdi mdi-star"></i>'
    half = '<i class="mdi mdi-star-half"></i>'
    empty = '<i class="mdi mdi-star-outline"></i>'
    stars = ''
    for _ in range(int(value)):
        stars += fullstar
    if value == 5:
        return mark_safe(stars)
    if value % 1 != 0:
        stars += half
    remain = 5 - value
    for _ in range(int(remain)):
        stars += empty
    return mark_safe(stars)


@register.filter
def count_properties(agent_name):
    qs = Listing.objects.filter(agent__user__username=agent_name).count()
    return qs

