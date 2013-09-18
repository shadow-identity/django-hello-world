from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django_hello_world.hello.models import Requests, State
from django.conf import settings


@receiver([post_save, post_delete])
def save_change_of_state(sender, **kwargs):
    if sender != State and sender in settings.HELLO_TABLES:
        rec_id = kwargs['instance'].id
        if not 'created' in kwargs:  # this was deletion
            State(record_id=rec_id, model=sender, state='deleted').save()
        elif kwargs['created']:  # creation of new record
            State(record_id=rec_id, model=sender, state='created').save()
        else:  # changing of existing record
            State(record_id=rec_id, model=sender, state='changed').save()
