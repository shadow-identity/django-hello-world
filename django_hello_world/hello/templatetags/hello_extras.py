from django import template

register = template.Library()


@register.tag(name="edit_link")
def do_get_admin_link(parser, token):
    """ parser
    """
    return GetAdminLinkNode('nope')


class GetAdminLinkNode(template.Node):
    def __init__(self, format_string):
        self.format_string = format_string

    def render(self, context):
        return self.format_string