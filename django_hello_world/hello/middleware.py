from django_hello_world.hello.models import Requests


class HelloMiddlewares(object):
    def process_request(self, request):
        Requests.objects.create(req=request,
                                url=request.build_absolute_uri(),
                                method=request.method,
                                user=request.user.username)
        return