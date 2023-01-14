from django import template

from myapp.models import Category
register = template.Library()

@register.simple_tag()
def get_cats():
    return Category.objects.all()