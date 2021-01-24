from django.shortcuts import render
from django.http import HttpResponse
from .models import Info, ContactMe, Projects
from .forms import ContactMeForm

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

def contactme(request):
    """Render contactme's page"""
    if request.method == 'POST':
        form = ContactMeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            new_data = ContactMe(email=email, subject=subject, message=message)
            new_data.save()
            context = {'form' : form}
            return render(request, 'portfolio/contactme.html', context)
    else:
        form = ContactMeForm()
        context = {'form' : form}
    return render(request, 'portfolio/contactme.html', context)