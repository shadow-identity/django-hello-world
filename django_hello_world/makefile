# Makefile
venv: activate
activate: ../requirements.txt
	test -d venv || virtualenv venv
	. ~/progs/venv/django-hello-world/bin/activate; pip install -Ur ../requirements.txt

dump:
	. ~/progs/venv/django-hello-world/bin/activate; python manage.py dumpdata hello.Contact auth.User --indent 4 > hello/fixtures/initial_data.json

full_dump:
	. ~/progs/venv/django-hello-world/bin/activate; python manage.py dumpdata --indent 4 > hello/fixtures/full_dump.json

full_test: dump
	. ~/progs/venv/django-hello-world/bin/activate; python manage.py test

test: full_dump
	. ~/progs/venv/django-hello-world/bin/activate; python manage.py test hello

shell:
	. ~/progs/venv/django-hello-world/bin/activate; python manage.py shell

run:
	. ~/progs/venv/django-hello-world/bin/activate; python manage.py runserver

south:
	. ~/progs/venv/django-hello-world/bin/activate; python manage.py schemamigration hello --auto
	. ~/progs/venv/django-hello-world/bin/activate; python manage.py migrate hello

makedb:
	-rm hello.sqlite3
	-. ~/progs/venv/django-hello-world/bin/activate; python manage.py syncdb --noinput
	. ~/progs/venv/django-hello-world/bin/activate; python manage.py migrate hello