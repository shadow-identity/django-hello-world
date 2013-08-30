from django.db.models.signals import post_save
from django.dispatch import receiver
from django_hello_world.hello.models import Requests


@receiver(post_save)
def limit_model(sender, **kwargs):
    Requests.objects.filter(id__gt=15).delete()



