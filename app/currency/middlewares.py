from time import time
from currency.models import ResponseLog
from django.core.handlers.wsgi import WSGIRequest


class SaveLogs:
    def __init__(self, get_response):
        self.get_response = get_response

    @staticmethod
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            _ip = x_forwarded_for.split(',')[0]
        else:
            _ip = request.META.get('REMOTE_ADDR')
        return _ip

    def __call__(self, request: WSGIRequest):
        start = time()
        response = self.get_response(request)
        end = time()
        responsetime = start - end

        query_p = None

        if request.method == 'GET':
            query_p = request.GET
        elif request.method == 'POST':
            query_p = request.POST

        log_data = ResponseLog(
            response_time=responsetime,
            request_method=request.method,
            query_params=query_p,
            ip=self.get_client_ip(request),
        )

        log_data.save()

        return response
