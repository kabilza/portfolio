from django.shortcuts import render
from django.http import HttpResponse
from .models import Info, ContactMe, Projects

# Create your views here.

def home(request):
    """Render homepage's page"""
    info = Info.objects.all()
    context = {'info' : info}
    return render(request, 'portfolio/homepage.html', context)