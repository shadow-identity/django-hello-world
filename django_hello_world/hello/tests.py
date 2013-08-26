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


class ContextProcessorTest(TestCase):
    def test_django_settings(self):
        from django.template import RequestContext
        from django.test.client import RequestFactory
        from django.conf import settings
        from hello.context_processors import django_settings

        factory = RequestFactory()
        request = factory.get('/')
        c = RequestContext(request, {'foo': 'bar'}, [django_settings])
        self.assertTrue('settings' in c)
        self.assertEquals(c['settings'], settings)