from django.forms import ModelForm
from django_hello_world.hello.models import Contact


class ContactForm(ModelForm):

    class Meta:
        model = Contact