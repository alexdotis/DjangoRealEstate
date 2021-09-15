from django import template
from listing.models import Listing
import urllib
from django.utils import timezone
import datetime
register = template.Library()


@register.filter
def subcategory_count(sub_name):
    return Listing.objects.filter(subcategory=sub_name).count()


@register.filter
def city_count(city_name):
    return Listing.objects.filter(city=city_name).count()

@register.filter
def status_count(status_name):
    return Listing.objects.filter(status=status_name).count()


@register.simple_tag(takes_context=True)
def url_query(context, **kwargs):
    request = context.get('request')
    get_copy = request.GET.copy()
    if get_copy.get('page'):
        get_copy.pop('page')
    get_copy.update(kwargs)
    return u'{path}?{params}'.format(path=request.path,
                params=urllib.parse.urlencode(get_copy, 'utf-8'))


@register.simple_tag()
def latest_updated_property_list():
    last_day = timezone.now() - datetime.timedelta(days=1)
    qs = Listing.objects.filter(updated_at__gt=last_day)
    return qs


@register.simple_tag()
def similar_properties (slug): 
    values =  Listing.objects.filter(slug=slug).values('city','property_type','status')
    qs = Listing.objects.filter(**values[0]).exclude(slug=slug)
    if qs.exists():
        return qs
    else:
        return Listing.objects.all()[:3]

    






