MANAGE=django-admin.py

test:
	-cd django_hello_world; PYTHONPATH=`pwd` python manage.py syncdb --noinput
	cd django_hello_world; PYTHONPATH=`pwd` python manage.py migrate hello
	cd django_hello_world; python manage.py dumpdata --indent 4 > hello/fixtures/full_dump.json
	cd django_hello_world; PYTHONPATH=`pwd` python manage.py test hello

run:
	cd django_hello_world; PYTHONPATH=`pwd` python manage.py runserver

syncdb:
	-cd django_hello_world; PYTHONPATH=`pwd` python manage.py syncdb --noinput
	cd django_hello_world; PYTHONPATH=`pwd` python manage.py migrate hello
