from authentication.models import Agent
from django import template
register = template.Library()


@register.simple_tag()
def trusted_agents():
    return Agent.objects.all()[:10]
