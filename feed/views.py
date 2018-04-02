from django.contrib.auth.decorators import login_required
from .models import *
import datetime
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect


# @login_required
def feed(request):
    return render(request, 'feed/feed.html', {})

# @login_required
def addPost(request):
    if request.method == "POST":
        post = Post();
        post.text = request.POST['post']
        post.published_date = timezone.now()
        post.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))