from django import template
from emarket.models import Category

register = template.Library()


@register.inclusion_tag('emarket/navcats.html')
def get_category_list():
    return {'navcats': Category.objects.all()}
