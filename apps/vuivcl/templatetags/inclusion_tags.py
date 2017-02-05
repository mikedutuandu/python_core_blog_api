
from django import template
from apps.vuivcl.models import Category

register = template.Library()

@register.inclusion_tag('vuivcl/inclusion_tags/_sidebar_list.html')
def sidebar_list():
    pass

@register.inclusion_tag('vuivcl/inclusion_tags/_nav_web.html')
def nav_web():
    categories = Category.objects.filter(enabled=True)
    return {'categories':categories}

@register.inclusion_tag('vuivcl/inclusion_tags/_nav_mobile.html')
def nav_mobile():
    return {}

