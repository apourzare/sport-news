from django import template
from ..models import Category
from basic_info.models import SiteSettings

register = template.Library()


@register.simple_tag
def site_title(name='param'):
    site = SiteSettings.objects.last()
    return site.site_title


@register.inclusion_tag('inc/category_navbar.html')
def category_navbar_2():
    print('*'*80)
    return {'categories' : Category.objects.all()}
    
