from django import template

register = template.Library()


@register.filter(name='edit_link')
def edit_link(value):
    return value