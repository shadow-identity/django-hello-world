from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django_hello_world.hello.models import Requests, State
from django.conf import settings


@receiver(post_save)
def limit_model(sender, **kwargs):
    if sender == Requests:
        count = Requests.objects.count()
        if count > 15:
            last_id = Requests.objects.values_list('id', flat=True)[count-1]
            Requests.objects.filter(id__lte=last_id-15).delete()
            if Requests.objects.count() > 15 and __debug__:
                print 'count       ', count
                print 'list id     ', Requests.objects.values_list('id', flat=True)
                print 'list filtred', Requests.objects.filter(id__lt=count-14).values_list('id', flat=True)
                print 'count_after ', Requests.objects.count()


@receiver([post_save, post_delete])
def save_change_of_state(sender, **kwargs):
    if sender != State and settings.HELLO_TABLES_EXISTS:
        rec_id = kwargs['instance'].id

        if not 'created' in kwargs:  # this was deletion
            print '1'
            State(record_id=rec_id, model=sender, state='deleted').save()
            print 'deleted'
        elif kwargs['created']:  # creation of new record
            print '2'
            import ipdb
            ipdb.set_trace()
            State(record_id=rec_id, model=sender, state='created').save()
            print 'created'
        else:  # changing of existing record
            print '3'
            State(record_id=rec_id, model=sender, state='changed').save()
            print 'changed'
