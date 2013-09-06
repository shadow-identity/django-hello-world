from django import template
from django.core import urlresolvers

register = template.Library()


@register.tag(name="edit_link")
def do_get_admin_link(parser, token):
    """ parser
    """
    try:
        tag_name, user_id = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError('%r tag argument requires a user id, got "%s"'
                                           % (token.contents.split()[0], (token.contents.split()[1:])))

    return GetAdminLinkNode(user_id)


class GetAdminLinkNode(template.Node):
    def __init__(self, user_id_var):
        self.user_id = template.Variable(user_id_var)

    def render(self, context):
        try:
            id = int(self.user_id.resolve(context))
            return urlresolvers.reverse('admin:hello_contact_change', args=(id,))
        except ValueError:
            return ''
