from django.http import HttpResponse
from django.template import loader

# Create your views here.
def hello(request):
    return HttpResponse(
        "<h1>Hello ABS</h1>"
        )

def about (request):
    return HttpResponse(
        "About"
        )