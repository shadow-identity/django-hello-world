from django.core.management.base import NoArgsCommand
from django.contrib.contenttypes.models import ContentType


class Command(NoArgsCommand):
    def handle_noargs(self, *args, **options):
        for ct in ContentType.objects.all():
            m = ct.model_class()
            str = "%s.%s\t%d" % (m.__module__, m.__name__, m._default_manager.count())
            print str
            self.stderr.write(str)