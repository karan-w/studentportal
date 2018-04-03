from django.contrib.auth.decorators import login_required
from .models import *
import datetime
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage


@login_required
def feed(request):
    return render(request, 'feed/feed.html', {})

# @login_required
def addPost(request):
    if request.method == "POST":
        post = Post();
        post.text = request.POST['post']
        post.published_date = timezone.now()
        if request.FILES['postImage']:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
        post.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))