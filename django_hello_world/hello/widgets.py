# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe


class DatePickerWidget(forms.DateInput):
    class Media:
        css = {
            'all': ("//code.jquery.com/ui/1.10.3/jquery-ui.js",)
        }
        js = (
            #settings.STATIC_URL+"js/jquery-1.7.1.min.js",
            "//code.jquery.com/jquery-1.10.2.min.js",
            #settings.STATIC_URL+"js/jquery-ui-1.8.17.custom.min.js",
            "//code.jquery.com/ui/1.10.3/jquery-ui.js",
            settings.STATIC_URL+"js/datepicker.js",
        )

    def __init__(self, params='', attrs=None):
        self.params = params
        super(DatePickerWidget, self).__init__(attrs=attrs)

    def render(self, name, value, attrs=None):
        rendered = super(DatePickerWidget, self).render(name, value, attrs=attrs)
        return rendered + mark_safe(u'''<script type="text/javascript">
            $('#id_%s').datepicker({%s});
            </script>'''%(name, self.params,))