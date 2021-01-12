from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    """Render homepage's page"""
    return render(request, 'portfolio/homepage.html')