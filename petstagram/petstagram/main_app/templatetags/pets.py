from django import template

from petstagram.main_app.models import Pet

register = template.Library()


@register.simple_tag()
def have_pets():
    return Pet.objects.count() > 0
