
from django import template
from apps.vuivcl.models import Category,Post

register = template.Library()

@register.inclusion_tag('vuivcl/inclusion_tags/_sidebar_list.html')
def sidebar_list():
    posts = Post.objects.filter(draft=False).order_by('-viewed_number')[0:20]
    return {'posts':posts}

@register.inclusion_tag('vuivcl/inclusion_tags/_nav_web.html')
def nav_web():
    categories = Category.objects.filter(enabled=True)
    return {'categories':categories}

@register.inclusion_tag('vuivcl/inclusion_tags/_nav_mobile.html')
def nav_mobile():

    categories = Category.objects.filter(enabled=True)
    return {'categories':categories}

