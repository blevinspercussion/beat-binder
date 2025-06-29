from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required

def home(request):
    context = {
        'year': datetime.now().year
    }
    return render(request, 'core/home.html', context)

@login_required
def about(request):
    context = {
        'year': datetime.now().year
    }
    return render(request, 'core/about.html', context)