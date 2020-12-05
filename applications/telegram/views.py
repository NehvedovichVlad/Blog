from django.contrib.sites import requests
from django.http import HttpResponse, HttpRequest
from django.views import View


def tg_view(requests: HttpRequest, *args, **kwargs):
    try:
        print(requests.body)
    finally:
        return HttpResponse()


class TgView(View):
    def post(self, request, *args, **kwargs):
        try:
            print(requests.body)
        finally:
            return HttpResponse()