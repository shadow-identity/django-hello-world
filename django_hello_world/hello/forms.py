from django.forms import ModelForm
from django import forms
from widgets import DatePickerWidget
from django_hello_world.hello.models import Contact, Requests


class ContactForm(ModelForm):

    class Meta:
        model = Contact
        widgets = {
            'date_of_birth': DatePickerWidget(params="dateFormat: 'yy-mm-dd', changeYear: true, "
                                                     "defaultDate: '-28y', yearRange: 'c-60:c+15'",
                                              attrs={'class': 'datepicker',}),
        }


#class RequestsForm(ModelForm):


#class CustomRequestsForm(ModelForm):
#    url = forms.URLField()
#    datetime = forms.DateTimeField()
#    method = forms.CharField()
#    user = forms.CharField()
#
#    class Meta(object):
#        model = Requests
#        fields = ['url', 'priority', 'datetime', 'method', 'user']




