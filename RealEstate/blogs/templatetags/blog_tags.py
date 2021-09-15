from django import template
from blogs.models import Blog


register = template.Library()


@register.simple_tag()
def topblogs():
    return Blog.objects.all().order_by('-created_at')[:3]


@register.simple_tag()
def get_blogs():
    return Blog.objects.all().order_by('-created_at')[:3]
