MANAGE=django-admin.py


test:
	ls
	ls django_hello_world
	ls django_hello_world/hello
	ls django_hello_world/hello/fixtures

	cd .. ; PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=django_hello_world.settings $(MANAGE) dumpdata --indent 4 > django_hello_world/hello/fixtures/full_dump.json
	cd .. ; PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=django_hello_world.settings $(MANAGE) test hello

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=django_hello_world.settings $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=django_hello_world.settings $(MANAGE) syncdb --noinput
