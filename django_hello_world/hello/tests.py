from StringIO import StringIO

from django.core.urlresolvers import reverse
from django.core.management import call_command
from django.test import TestCase
from django.conf import settings
from django.template import RequestContext, Template, Context
from django.test.client import RequestFactory
from django.contrib.contenttypes.models import ContentType

from django_hello_world.hello.models import Requests, Contact, State
from django_hello_world.settings import rel
from django_hello_world.hello.context_processors import django_settings, get_settings_dict
from django_hello_world.hello.middleware import HelloMiddlewares

hello_fixtures_file = [rel(settings.FIXTURE_DIRS[0], 'test_data.json')]


class HelloViewsTest(TestCase):
    fixtures = hello_fixtures_file

    def setUp(self):
        self.somevalue = 'blablabla'
        self.valid_form = {'name': self.somevalue,
                           'surname': 'b',
                           'email': 'a@c.com',
                           'jabber': 'b@c.com',
                           'date_of_birth': '1985-02-17',
                           'skype': 'lksdl',
                           'photo': 'dlskf',
                           'other_contacts': 'd',
                           'bio': 'd'}

    def test_hello(self):
        """ Tests that contact information is shown on the home page
        """
        response = self.client.get(reverse('home'))
        surname_from_db = Contact.objects.get(id=1).surname
        self.assertContains(response, surname_from_db, status_code=200)

    def test_last_10_records_show(self):
        """ Test that we get 10 last records with requests on /requests page
        """
        response = self.client.post(reverse('requests'))

        for record in Requests.objects.reverse()[:10]:  # read last 10 Requests:
            date_and_time_formatted = Requests.objects.latest('pk').datetime.strftime('%Y %B %d, %H:%M')
            self.assertContains(response, date_and_time_formatted)
            self.assertContains(response, Requests.objects.latest('pk').user)
            self.assertContains(response, Requests.objects.latest('pk').url)
            self.assertContains(response, Requests.objects.latest('pk').method)
            self.assertContains(response, Requests.objects.latest('pk').priority)


    def test_not_logged(self):
        """ Test that correct form without authentication = redirect to login page
        """
        response = self.client.post(reverse('form'), self.valid_form, follow=True)
        self.assertFalse(Contact.objects.filter(name=self.somevalue).exists())  # not in base
        self.assertEqual(response.redirect_chain[0][1], 302)  # it was redirect
        self.assertEqual(response.status_code, 200)  # and it was ok
        self.assertTrue(reverse('login') in response.redirect_chain[0][0])  # and to right destination
        self.assertRedirects(response, reverse('login') + '?next=/accounts/profile/', status_code=302,
                             target_status_code=200)

    def test_login_and_save_correct(self):
        """ Test that correct data saved and redirect to Success page
        """
        self.client.login(username='admin', password='admin')
        response = self.client.post(reverse('form'), self.valid_form, follow=True)
        self.assertTrue(Contact.objects.filter(name=self.somevalue).exists())  # somevalue in base
        self.assertContains(response, 'Success')

    def test_login_and_save_invalid(self):
        """ Test that incorrect data don't saved and reported to user """
        self.client.login(username='admin', password='admin')
        self.valid_form['email'] = 'blablabla'
        response = self.client.post(reverse('form'), self.valid_form)
        self.assertFalse(Contact.objects.filter(name=self.somevalue).exists())  # new values don't saved
        self.assertContains(response, 'Enter a valid email address.')

    def test_save_empty(self):
        """ Test that empty data field don't saved and reported to user """
        self.client.login(username='admin', password='admin')
        self.valid_form['email'] = ''
        response = self.client.post(reverse('form'), self.valid_form)
        self.assertFalse(Contact.objects.filter(name=self.somevalue).exists())  # new values don't saved
        self.assertContains(response, 'This field is required')


class HelloDBManipulationsTest(TestCase):
    fixtures = hello_fixtures_file

    def test_save_request_to_db(self):
        """ Test that we really save requests to db
        """
        class MockUser():
            """ mock class to imitate .user.username attribute in requests """
            def __init__(self):
                self.username = 'MockUser'

        test_value = 'sdoifso'

        factory = RequestFactory()
        request = factory.get(reverse('home'), data={'test': test_value})
        request.user = MockUser()
        HelloMiddlewares().process_request(request)

        data_from_db = Requests.objects.reverse()[0].req
        self.assertTrue(test_value in data_from_db)

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


class HelloUtilsTest(TestCase):
    fixtures = hello_fixtures_file

    def test_tag_edit_link(self):
        """ Test that tag 'edit_link' works properly """
        template = Template('{% load hello_extras %}{% edit_link record %}')
        factory = RequestFactory()
        request = factory.get(reverse('home'))
        # Send context that contains needed information to tag
        context = Context(RequestContext(request, {'record': Contact.objects.get(pk=1)}))

        example = '/admin/hello/contact/1/'
        self.assertTrue(example in template.render(context))

    def test_django_settings(self):
        """ Test context processor 'django_settings'
        """
        factory = RequestFactory()
        request = factory.get('/')
        RequestContext(request, [django_settings])

        settings = get_settings_dict()
        for setting in settings:
            self.assertEqual(RequestContext(request).get(setting), settings[setting])

    def test_command_show_models_objects(self):
        """ Tests that commend 'show_models_objects' shows everything that should
        """
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
        Requests.objects.create(req='test', priority=1)
        self.assertFalse(compare(out))
