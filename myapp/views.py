from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    return HttpResponse(
        "<h1>INDEX PAGE</h1>"
        )

def hello(request, username):
    print(username)
    return HttpResponse(
        "<h1>Hello %s</h1>" %username
        )

def about (request):
    return HttpResponse(
        "About"
        )