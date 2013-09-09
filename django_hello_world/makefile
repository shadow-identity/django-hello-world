# Makefile
venv: activate
activate: ../requirements.txt
	test -d venv || virtualenv venv
	. ~/progs/venv/django-hello-world/bin/activate; pip install -Ur ../requirements.txt

dump:
	. ~/progs/venv/django-hello-world/bin/activate; python manage.py dumpdata -e contenttypes --indent 4 > hello/fixtures/initial_data.json

full_test: dump
	. ~/progs/venv/django-hello-world/bin/activate; python manage.py test

test: dump
	. ~/progs/venv/django-hello-world/bin/activate; python manage.py test hello

shell:
	. ~/progs/venv/django-hello-world/bin/activate; python manage.py shell

run:
	. ~/progs/venv/django-hello-world/bin/activate; python manage.py runserver

south:
	. ~/progs/venv/django-hello-world/bin/activate; python manage.py --settings=django_hello_world.settings_db_change schemamigration hello --auto
	. ~/progs/venv/django-hello-world/bin/activate; python manage.py migrate hello

makedb:
	# kostyl na kostyle kostylem pogonaet
	-. ~/progs/venv/django-hello-world/bin/activate; python manage.py syncdb --settings=django_hello_world.settings_db_change
	. ~/progs/venv/django-hello-world/bin/activate; python manage.py migrate hello --settings=django_hello_world.settings_db_change