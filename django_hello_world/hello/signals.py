from django.db.models.signals import post_save
from django.dispatch import receiver
from django_hello_world.hello.models import Requests


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
                import ipdb
                ipdb.set_trace()


