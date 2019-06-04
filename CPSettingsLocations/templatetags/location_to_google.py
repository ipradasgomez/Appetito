from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def location_to_valid_google(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value.replace(" ", "+")