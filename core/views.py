from django.shortcuts import render
from datetime import datetime

def home(request):
    context = {
        'year': datetime.now().year
    }
    return render(request, 'core/home.html', context)

def about(request):
    context = {
        'year': datetime.now().year
    }
    return render(request, 'core/about.html', context)