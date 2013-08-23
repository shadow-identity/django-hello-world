from annoying.decorators import render_to
from django.contrib.auth.models import User


@render_to('hello/home.html')
def home(request):
    users = User.objects.filter()

    from hello.models import Contact
    record = Contact.objects.get(pk=1)

    return {'users': users,
            'name': record.name,
            'surname': record.surname,
            'bio': record.bio,
            'skype': record.skype,
            'email': record.email,
            'jabber': record.jabber,
            'other_contacts': record.other_contacts,
            'date_of_birth': record.date_of_birth}
