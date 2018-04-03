from django.contrib.auth.decorators import login_required
from .models import *
import datetime
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# def image_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/feed_<id>/<filename>
#     return 'feed_{0}/{1}'.format(instance.user.id, filename)

@login_required
def feed(request):
    posts_list = Post.objects.all().order_by('-published_date')[:50]
    paginator = Paginator(posts_list, 10)

    page = request.GET.get('page', 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'feed/feed.html', {'posts':posts})

@login_required
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

def search_posts(request):
    if request.method == "POST":
        posts_list = Post.objects.filter(text__iexact=request.POST['search_text'])[:50]
        paginator = Paginator(posts_list, 10)

        page = request.GET.get('page', 1)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        return render(request, 'feed/searchresults.html', {'posts': posts})
