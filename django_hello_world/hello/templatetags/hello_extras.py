from django import template

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

    return GetAdminLinkNode(user_id[1:-1])


class GetAdminLinkNode(template.Node):
    def __init__(self, user_id):
        print 'fuck you'
        self.user_id = template.Variable(user_id)
        print type(self.user_id), self.user_id

    def render(self, context):
        try:
            self.user_id = int(self.user_id)
            return self.user_id
        except ValueError:
            return ''


