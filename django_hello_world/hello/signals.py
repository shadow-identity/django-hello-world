from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings

from django_hello_world.hello.models import State


@receiver([post_save, post_delete])
def save_change_of_state(sender, **kwargs):
    if sender != State and sender in settings.HELLO_TABLES:
        rec_id = kwargs['instance'].id
        if not 'created' in kwargs:  # this was deletion
            State.objects.create(record_id=rec_id, model=str(sender), state='deleted')
        elif kwargs['created']:  # creation of new record
            State.objects.create(record_id=rec_id, model=str(sender), state='created')
        else:  # changing of existing record
            State.objects.create(record_id=rec_id, model=str(sender), state='changed')
