"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client

from random import random
from django_hello_world.hello.models import Requests


class HttpTest(TestCase):
    fixtures = ['hello/fixtures/dump.json']

    def test_hello(self):
        c = Client()
        response = c.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Pavel')


class MiddlewareTest(TestCase):
    fixtures = ['hello/fixtures/dump.json']

    def setUp(self):
        self.c = Client()
        self.rnd = str(random())

    def test_save_request_to_db(self):
        """ Test that we really save requests to db
        """
        self.c.post('/', {'random': self.rnd})
        data_from_db = Requests.objects.reverse()[0].req
        self.assertTrue(self.rnd in data_from_db)

    def test_last_10_records_show(self):
        """ Test that we get 10 last records with requests on /requests page
        """
        response = self.c.post(reverse('requests'))
        text = ''
        for record in Requests.objects.reverse()[:10]:
            text = record.req
        self.assertTrue(response.content, text)

    def test_limit_requests(self):
        """ Test that we limit Requests table by 15 records
        """
        for i in range(0, 15):
            self.c.get('/')
        self.assertTrue(Requests.objects.count() <= 15)


class ContextProcessorTest(TestCase):
    def test_django_settings(self):
        from django.template import RequestContext
        from django.test.client import RequestFactory
        from django_hello_world.hello.context_processors import django_settings, get_settings_dict

        factory = RequestFactory()
        request = factory.get('/')
        RequestContext(request, [django_settings])

        settings = get_settings_dict()
        for setting in settings:
            self.assertEqual(RequestContext(request).get(setting), settings[setting])
