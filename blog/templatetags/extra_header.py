from django import template
from ..models import Category
from basic_info.models import SiteSettings

register = template.Library()


@register.simple_tag()
def site_setting():
    return SiteSettings.objects.last()


@register.inclusion_tag('inc/category_navbar.html')
def category_navbar():
    return {
        'categories': Category.objects.all()
    }
