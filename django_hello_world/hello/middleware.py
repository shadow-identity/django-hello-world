from django_hello_world.hello.models import Requests
from datetime import datetime

class HelloMiddlewares(object):

    def process_request(self, request):
        Requests(req=request).save()
        print 'url      ', request.build_absolute_uri()
        print 'datetime ', datetime.utcnow()
        print 'method   ', request.method
        if request.user.is_authenticated():
            print 'user     ', request.user.username
        else:
            print 'user     ', 'anonymous'

        return