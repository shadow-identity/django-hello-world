from django.forms import ModelForm
from django import forms

from django_hello_world.hello.models import Contact, Requests


class ContactForm(ModelForm):

    class Meta:
        model = Contact


class CustomRequestsForm(ModelForm):
    url = forms.URLField()
    datetime = forms.DateTimeField()
    method = forms.CharField()
    user = forms.CharField()

    class Meta(object):
        model = Requests
        fields = ['url', 'priority', 'datetime', 'method', 'user']




