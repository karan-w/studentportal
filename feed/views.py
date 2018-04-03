from django.contrib.auth.decorators import login_required
from .models import *
import datetime
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage


# def image_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/feed_<id>/<filename>
#     return 'feed_{0}/{1}'.format(instance.user.id, filename)

@login_required
def feed(request):
    return render(request, 'feed/feed.html', {})

# @login_required
def add_post(request):
    if request.method == "POST":
        post = Post()
        post.user = request.user
        post.text = request.POST['text']
        post.published_date = timezone.now()
        post.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    if request.FILES['postImage'] and request.method == "POST":
        post = Post()
        post.user = request.user
        post.text = request.POST['text']
        post.published_date = timezone.now()
        myfile = request.FILES['postImage']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))