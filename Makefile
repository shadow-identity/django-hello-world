MANAGE=django-admin.py

test:
	cd django_hello_world; python manage.py syncdb --noinput
	cd django_hello_world; python manage.py dumpdata --indent 4 > hello/fixtures/full_dump.json
	cd django_hello_world; PYTHONPATH=`pwd` python manage.py test hello


run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=django_hello_world.settings $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=django_hello_world.settings $(MANAGE) syncdb --noinput