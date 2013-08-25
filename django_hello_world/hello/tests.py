"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client

from random import random
from hello.models import Requests


class HttpTest(TestCase):
    fixtures = ['hello/fixtures/dump.json']

    def test_hello(self):
        c = Client()
        response = c.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Pavel')


class MiddlewareTest(TestCase):
    fixtures = ['hello/fixtures/dump.json']

    def test_save_request_to_db(self):
        c = Client()
        rnd = str(random())
        c.post('/', {'random': rnd})
        data_from_db = Requests.objects.reverse()[1].req
        self.assertTrue(rnd in data_from_db)