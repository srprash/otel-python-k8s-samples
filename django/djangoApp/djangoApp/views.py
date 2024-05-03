import requests
from django.http import HttpResponse
import os, sys

def healthcheck(request):
    path = sys.path
    return HttpResponse("healthcheck:: PATH:: " + str(path))


def http_call(request):
    requests.get("https://aws.amazon.com")
    return HttpResponse("[Django] Ok! tracing outgoing http call")