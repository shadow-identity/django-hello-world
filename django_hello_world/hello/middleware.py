from django_hello_world.hello.models import Requests
from datetime import datetime


class HelloMiddlewares(object):

    def process_request(self, request):

        import ipdb
        ipdb.set_trace()

        if request.user.is_authenticated():
            Requests(req=request,
                     url=request.build_absolute_uri(),
                     method=request.method,
                     user=request.user.username).save()
        else:
            Requests(req=request,
                     url=request.build_absolute_uri(),
                     method=request.method,
                     user=None).save()
        return