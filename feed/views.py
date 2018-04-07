from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from .models import *
import datetime
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# def image_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/feed_<id>/<filename>
#     return 'feed_{0}/{1}'.format(instance.user.id, filename)


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
    print(len(posts_list))
    paginator = Paginator(posts_list, 10)
    page = request.GET.get('page', 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
   
    obj = Signup.objects.get(username=request.user)
    
    objsub = obj.subjects.split(',',100)
    print(objsub)

    mylist = list()
    for x in objsub:
        y = Subject.objects.get(subjectid=x)
        if obj.category == 'cr':
            y.cr = True
        else:
            y.cr = False 
        mylist.append(y)
    return render(request, 'feed/feed.html', {'posts':posts,'sublist':mylist})

def show_timetable(request):
    if request.method == "POST":
         d = request.POST['userdate']
         obj = Signup.objects.get(username=request.user)
         objsub = obj.subjects.split(',',100)
         mylist1 = list()
         for x in objsub:
            y = timetable.objects.get(subjectid=x,date=d)
            mylist1.append(y)

    sorted(mylist1, key=lambda s: s.startTime)
    return render(request, 'feed/feed.html', {'ttable':mylist1})
            


@login_required
def add_post(request):
    if request.method == "POST":
        post = Post()
        post.user = request.user
        post.text = request.POST['text']
        post.published_date = timezone.now()              
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
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def add_time_table(request):
     if request.method == "POST":
        d = request.POST['hiddendate']
        print(d)
        sid = request.POST['tthiddentext']
        ttf = timetable.objects.filter(date=d,subjectid=sid) 
        if not ttf:
            tt= timetable()
        else:    
            tt = timetable.objects.get(date=d,subjectid=sid)
        
        
        tt.subjectid=sid
        tt.date=d
        tt.startTime= request.POST['starttime']
        tt.endTime = request.POST['endtime']
        tt.classType=''
        a= request.POST['cl']

        if a!='slot':
            tt.classType = tt.classType + a

        a=request.POST['exam']

        if a!='Noexam':
            tt.classType = tt.classType + a

        a=request.POST['Other']

        if a:
            tt.classType = tt.classType + a
        
        tt.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
def add_assign_link(request):
     if request.method == "POST":
         a = request.POST['hiddentext']
         subject = Subject.objects.filter(subjectid=a)
         for sub in subject:
             sub.assignments = request.POST['aslink']
             sub.save()    
         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))       

def add_notes_link(request):
     if request.method == "POST":
         a = request.POST['nthiddentext']
         subject = Subject.objects.filter(subjectid=a)
         for sub in subject:
             sub.notes = request.POST['ntlink']
             sub.save()    
         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))       

def add_prev_link(request):
     if request.method == "POST":
         a = request.POST['prhiddentext']
         print(a)
         subject = Subject.objects.filter(subjectid=a)
         for sub in subject:
             sub.prevpapers = request.POST['prlink']
             sub.save()    
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


