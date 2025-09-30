from django.http import HttpResponse
from .models import Task, Project
from django.shortcuts import render

# Create your views here.

def index(request):
    title = 'Django Course!!!'
    return render(request, 'index.html', {'title': title})

def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello %s</h1>" %username)

def about (request):
    username = 'wels'
    #username = {'name':'wels'}
    return render(request, 'about.html',{
        'username': username
    })

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request,'projects.html',{
        'projects':projects
    })

def tasks(request):
    #tasks = Task.objects.get()
    return render(request,'tasks.html')