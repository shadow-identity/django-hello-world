from django.core.urlresolvers import reverse
from django.core.management import call_command
from django.test import TestCase
from django.test.client import Client
from random import random
from django_hello_world.hello.models import Requests, Contact, State
from django_hello_world.settings import rel
from django.conf import settings
from StringIO import StringIO
from django.template import RequestContext
from django.test.client import RequestFactory
from django_hello_world.hello.context_processors import django_settings, get_settings_dict
from django.contrib.contenttypes.models import ContentType

hello_fixtures_file = [rel(settings.FIXTURE_DIRS[0], 'full_dump.json')]


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
        response = self.client.get(reverse('home'))
        surname_from_db = Contact.objects.get(id=1).surname
        self.assertContains(response, surname_from_db, status_code=200)

    def test_save_request_to_db(self):
        """ Test that we really save requests to db
        """
        self.client.post('/', {'random': self.rnd})
        data_from_db = Requests.objects.reverse()[0].req
        self.assertTrue(self.rnd in data_from_db)

    def test_last_10_records_show(self):
        """ Test that we get 10 last records with requests on /requests page
        """
        response = self.client.post(reverse('requests'))
        text = ''
        for record in Requests.objects.reverse()[:10]:
            text = record.req
        self.assertTrue(response.content, text)

    def test_not_logged(self):
        """ Test that correct form without authentication = redirect to login page
        """
        response = self.client.post(reverse('form'), self.valid_form, follow=True)
        self.assertFalse(Contact.objects.filter(name=self.rnd).exists())  # not in base
        self.assertEqual(response.redirect_chain[0][1], 302)  # it was redirect
        self.assertEqual(response.status_code, 200)  # and it was ok
        self.assertTrue(reverse('login') in response.redirect_chain[0][0])  # and to right destination

    def test_login_and_save_correct(self):
        """ Test that correct data saved and redirect to Success page
        """
        self.client.login(username='admin', password='admin')
        response = self.client.post(reverse('form'), self.valid_form, follow=True)
        self.assertTrue(Contact.objects.filter(name=self.rnd).exists())  # rnd in base
        self.assertContains(response, 'Success')

    def test_login_and_save_invalid(self):
        """ Test that incorrect data don't saved and reported to user """
        self.client.login(username='admin', password='admin')
        self.valid_form['email'] = 'blablabla'
        response = self.client.post(reverse('form'), self.valid_form)
        self.assertFalse(Contact.objects.filter(name=self.rnd).exists())  # new values don't saved
        self.assertContains(response, 'Enter a valid email address.')

    def test_save_empty(self):
        """ Test that empty data field don't saved and reported to user """
        self.client.login(username='admin', password='admin')
        self.valid_form['email'] = ''
        response = self.client.post(reverse('form'), self.valid_form)
        self.assertFalse(Contact.objects.filter(name=self.rnd).exists())  # new values don't saved
        self.assertContains(response, 'This field is required')

    def test_tag_edit_link(self):
        """ Test that tag 'edit_link' works properly """
        response = self.client.get('/')
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
        tst_msg = 'created'
        record = Requests(req=tst_msg)  # Creating record
        record.save()
        last_instance = State.objects.latest('pk')
        self.assertEqual([last_instance.state, last_instance.record_id, last_instance.model],
                         [unicode(tst_msg), record.pk, unicode(Requests)])
        tst_msg = 'changed'
        record.req = 'fuck'
        record.save()
        last_instance = State.objects.latest('pk')
        self.assertEqual([last_instance.state, last_instance.record_id, last_instance.model],
                         [unicode(tst_msg), record.pk, unicode(Requests)])
        tst_msg = 'deleted'
        last_pk = record.pk
        record.delete()
        last_instance = State.objects.latest('pk')
        self.assertEqual([last_instance.state, last_instance.record_id, last_instance.model],
                         [unicode(tst_msg), last_pk, unicode(Requests)])

    def test_command_show_models_objects(self):
        def compare(command_output):
            """ compare every string in output with all objects
            """
            for (i, table) in enumerate(ContentType.objects.all()):
                testing_string = "%s.%s\t%d" % (table.model_class().__module__,
                                                table.model_class().__name__,
                                                table.model_class()._default_manager.count())
                if testing_string != command_output.getvalue().splitlines()[i]:
                    return False
            return True

        out = StringIO()
        err = StringIO()
        call_command('show_models_objects', stdout=out, stderr=err)
        self.assertEqual(out.getvalue(), err.getvalue())
        self.assertTrue(compare(out))
        # self-test
        Requests(req='test', priority=1).save()
        self.assertFalse(compare(out))
