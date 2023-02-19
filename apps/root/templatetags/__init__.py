from django import template

register = template.Library()

@register.filter
def attr(dictlike, key): # Django is stupid
    if isinstance(dictlike, dict):
        return dictlike.get(key, None)
    return getattr(dictlike, key, '')
