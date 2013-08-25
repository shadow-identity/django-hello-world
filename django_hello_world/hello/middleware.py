from hello.models import Requests


class HelloMiddlewares(object):

    def process_request(self, request):
        return