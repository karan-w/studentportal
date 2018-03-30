from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

# @login_required
def feed(request):
    return render(request, 'feed/feed.html', {})

