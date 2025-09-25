from django.http import HttpResponse, JsonResponse
from .models import Task, Project

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

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request,id):
    tasks = Task.objects.get(id=id)
    return HttpResponse('task: %s' % tasks.title)