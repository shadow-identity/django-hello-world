from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from django_hello_world import hello
from random import random
from django_hello_world.hello.models import Requests, Contact, State
from django_hello_world.settings import rel
from django.conf import settings

from django.template import RequestContext
from django.test.client import RequestFactory
from django_hello_world.hello.context_processors import django_settings, get_settings_dict

hello_fixtures_file = [rel(settings.FIXTURE_DIRS[0], 'initial_data.json')]


class HelloTest(TestCase):
    fixtures = hello_fixtures_file

    def setUp(self):
        self.c = Client()
        self.rnd = str(random())
        self.valid_form = {'name': self.rnd,
                           'surname': 'b',
                           'email': 'a@c.com',
                           'jabber': 'b@c.com',
                           'date_of_birth': '1985-02-17',
                           'skype': 'lksdl',
                           'photo': 'dlskf',
                           'other_contacts': 'd',
                           'bio': 'd'}

    def test_hello(self):
        response = self.c.get(reverse('home'))
        self.assertContains(response, 'Pavel', status_code=200)

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

    def test_not_logged(self):
        """ Test that correct form without authentication = redirect to login page
        """
        response = self.c.post(reverse('form'), self.valid_form, follow=True)
        self.assertFalse(Contact.objects.filter(name=self.rnd).exists())  # not in base
        self.assertEqual(response.redirect_chain[0][1], 302)  # it was redirect
        self.assertEqual(response.status_code, 200)  # and it was ok
        self.assertTrue(reverse('login') in response.redirect_chain[0][0])  # and to right destination

    def test_login_and_save_correct(self):
        """ Test that correct data saved and redirect to Success page
        """
        self.c.login(username='admin', password='admin')
        response = self.c.post(reverse('form'), self.valid_form, follow=True)
        self.assertTrue(Contact.objects.filter(name=self.rnd).exists())  # rnd in base
        self.assertContains(response, 'Success')

    def test_login_and_save_invalid(self):
        """ Test that incorrect data don't saved and reported to user """
        self.c.login(username='admin', password='admin')
        self.valid_form['email'] = 'blablabla'
        response = self.c.post(reverse('form'), self.valid_form)
        self.assertFalse(Contact.objects.filter(name=self.rnd).exists())  # new values don't saved
        self.assertContains(response, 'Enter a valid email address.')

    def test_save_empty(self):
        """ Test that empty data field don't saved and reported to user """
        self.c.login(username='admin', password='admin')
        self.valid_form['email'] = ''
        response = self.c.post(reverse('form'), self.valid_form)
        self.assertFalse(Contact.objects.filter(name=self.rnd).exists())  # new values don't saved
        self.assertContains(response, 'This field is required')

    def test_tag_edit_link(self):
        """ Test that tag 'edit_link' works properly """
        response = self.c.get('/')
        example = '/admin/hello/contact/1/">(admin)</a>'
        self.assertContains(response, example, status_code=200)

    def test_django_settings(self):
        """ Test context processor 'django_settings'
        """
        factory = RequestFactory()
        request = factory.get('/')
        RequestContext(request, [django_settings])

        settings = get_settings_dict()
        for setting in settings:
            self.assertEqual(RequestContext(request).get(setting), settings[setting])

    def test_saving_state(self):
        """ Test that we are saving state of records correctly
        """
        tst_msg = 'blablabla'
        Requests(req=tst_msg).save()  # Creating record
        last_instance = State.objects.get(pk__max)
        self.assertEqual([last_instance.state, last_instance.record_id, last_instance.model], [tst_msg, 0, Requests])
        tst_msg = 'fufufu'
        #Requests(req=tst_msg).save()  # Changing record
        #self.assertEqual(State.objects.get(id=0).state, tst_msg)