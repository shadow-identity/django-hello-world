from django.forms import ModelForm
from widgets import DatePickerWidget
from django_hello_world.hello.models import Contact


class ContactForm(ModelForm):

    class Meta:
        model = Contact
        widgets = {
            'date_of_birth': DatePickerWidget(params="dateFormat: 'yy-mm-dd', changeYear: true, "
                                                     "defaultDate: '-28y', yearRange: 'c-60:c+15'",
                                              attrs={'class': 'datepicker'}),
        }