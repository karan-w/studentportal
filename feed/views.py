from __future__ import unicode_literals

from json.decoder import PosInf

from django.contrib.auth.decorators import login_required
from .models import *
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import FormView
from .forms import *
from django.http import JsonResponse
from .forms import *


def image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/feed_<id>/<filename>
    return 'feed_{0}/{1}'.format(instance.user.id, filename)


def check_if_faculty(user):
    if user.groups.filter(name="Faculty").exists():
        return True
    else:
        return False

def check_if_CA_secretary(user):
    if user.groups.filter(name="CASecretary").exists():
        return True
    else:
        return False

def check_if_sports_secretary(user):
    if user.groups.filter(name="SportsSecretary").exists():
        return True
    else:
        return False
def check_if_class_representative(user):
    if user.groups.filter(name="ClassRepresentative").exists():
        return True
    else:
        return False

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

    form = PostForm()
    return render(request, 'feed/feed.html', {'posts':posts})
            


@login_required
def add_post(request):
    if request.method == "POST":
        post = Post()
        post.text = request.POST['text']
        post.user = request.user
        if check_if_CA_secretary(request.user):
            post.category = 'CA'
        elif check_if_class_representative(request.user):
            post.category = 'CR'
        elif check_if_faculty(request.user):
            post.category = 'AC'
        elif check_if_sports_secretary(request.user):
            post.category = 'SP'
        else:
            post.category = 'GN'
        post.save()
        photos = request.FILES.getlist('images')
        for photo in photos:
            p = Photo()
            p.post = post
            p.file = photo
            p.save()
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

def academics_posts(request):
    posts_list = Post.objects.filter(category__contains='AC')[:50]
    paginator = Paginator(posts_list, 10)

    page = request.GET.get('page', 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'feed/academics.html', {'posts': posts})

def clubs_and_association_posts(request):
    posts_list = Post.objects.filter(category__contains='CA')[:50]
    paginator = Paginator(posts_list, 10)

    page = request.GET.get('page', 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'feed/clubsassociations.html', {'posts': posts})

def sports_posts(request):
    posts_list = Post.objects.filter(category__contains='SP')[:50]
    paginator = Paginator(posts_list, 10)

    page = request.GET.get('page', 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'feed/sports.html', {'posts': posts})

class AddPostView(FormView):
    def get(self, request):
        photos_list = Photo.objects.all()
        return HttpResponseRedirect('/')

    def post(self, request):
        print(request.POST['images'])
        print(request.FILES)
        form = PostForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)