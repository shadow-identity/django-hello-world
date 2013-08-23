"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client


class HttpTest(TestCase):
    fixtures = ['hello/fixtures/dump.json']
    def test_hello(self):
        c = Client()
        response = c.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Pavel')
