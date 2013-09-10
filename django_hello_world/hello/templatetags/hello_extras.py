from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag(takes_context=True, name='edit_link')
def get_admin_link(context, record):
    """ create hyperlink to admin edit of record by uid """
    rel_url = reverse('admin:%s_%s_change' % (record._meta.app_label,  record._meta.module_name),  args=(record.id,))
    abs_url = context['request'].build_absolute_uri(rel_url)
    return abs_url