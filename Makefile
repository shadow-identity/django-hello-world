MANAGE=django-admin.py

test:
	-rm django_hello_world/hello.sqlite3
	-cd django_hello_world; PYTHONPATH=`pwd` python manage.py syncdb --noinput
	cd django_hello_world; PYTHONPATH=`pwd` python manage.py migrate hello
	cd django_hello_world; python manage.py dumpdata --indent 4 > hello/fixtures/full_dump.json
	cd django_hello_world; PYTHONPATH=`pwd` python manage.py test hello

run:
	-rm django_hello_world/hello.sqlite3
	-cd django_hello_world; PYTHONPATH=`pwd` python manage.py syncdb --noinput
	cd django_hello_world; PYTHONPATH=`pwd` python manage.py migrate hello
	cd django_hello_world; PYTHONPATH=`pwd` python manage.py runserver

syncdb:
	-rm django_hello_world/hello.sqlite3
	-cd django_hello_world; PYTHONPATH=`pwd` python manage.py syncdb --noinput
	cd django_hello_world; PYTHONPATH=`pwd` python manage.py migrate hello
