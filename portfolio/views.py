from django.shortcuts import render
from django.http import HttpResponse
from .models import Info, ContactMe, Projects

# Create your views here.

def home(request):
    """Render homepage's page"""
    info = Info.objects.all()
    context = {'info' : info}
    return render(request, 'portfolio/homepage.html', context)

def projects(request):
    """Render projects's page"""
    projects = Projects.objects.all()
    context = {'projects' : projects}
    return render(request, 'portfolio/projects.html', context)