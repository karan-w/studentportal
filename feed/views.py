from __future__ import unicode_literals

from json.decoder import PosInf
import datetime
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import *
from authentication.models import *
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import FormView
from django.http import JsonResponse
from polls.models import Question


# href="/media/{{ i.url }}"
def get_post_image_path(instance,filename):
	return 'posts/{0}/{1}'.format(instance.post.user.username,filename)


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
    questions = Question.objects.order_by('-pub_date')[:5]
    choices = []
    choices_list = []

    for question in questions:
        choices = question.choices.all()
        for choice in choices:
            choices_list.append(choice)

    print(choices_list)

    posts_list = Post.objects.all().order_by('-published_date')[:50]
    images = []
    for postobj in posts_list:
        i = Photo.objects.filter(post=postobj)
        for j in i:
            images.append(j)

    print(len(images))
    paginator = Paginator(posts_list, 10)
    page = request.GET.get('page', 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    
    student=Student.objects.get(user=request.user)
    print(student)
    courses = Course.objects.filter(semester = student.semester, department = student.branch)
    if check_if_class_representative(request.user):
        print("cr")
        return render(request, 'feed/cr_feed.html', {'posts':posts, 'images': images, 'courses':courses})
    else:
        print("not cr")
        print(student.semester)
        print(student.branch)
        print(courses)
        
        tt = Timetable.objects.get(section=student.section, year=student.year, semester=student.semester)
    return render(request, 'feed/feed.html', {'posts': posts, 'images': images, 'questions': questions, 'n' : range(5), 'choices':choices_list, 'tt':tt, 'courses':courses})

def update_timetable(request):
    if request.method=='POST':
        student = Student.objects.get(user=request.user)
        check = Timetable.objects.filter(section=student.section, year=student.year, semester=student.semester)
        print(check)
        if check.count()!=0:
         tt = Timetable.objects.get(section=student.section, year=student.year, semester=student.semester)
        else:
         tt= Timetable()
        tt.course8_9=request.POST['8-9']
        tt.course9_10=request.POST['9-10']
        tt.course10_11=request.POST['10-11']
        tt.course11_12=request.POST['11-12']
        tt.course12_1=request.POST['12-1']
        tt.course2_3=request.POST['2-3']
        tt.course3_4=request.POST['3-4']
        tt.course4_5=request.POST['4-5']
        #tt.date = request.POST['ttdate']
        tt.date=request.POST['timetabledate']
        tt.section = student.section
        tt.year = student.year
        tt.semester = student.semester
        tt.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def add_post(request):
    if request.method == "POST":
        post = Post()
        post.published_date = timezone.now()
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
            p.url = get_post_image_path(p, p.file)
            p.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def search_posts(request):
    if request.method == "POST":
        posts_list = Post.objects.filter(text__iexact=request.POST['search_text'])[:50]
        images = []
        for postobj in posts_list:
            i = Photo.objects.filter(post=postobj)
            for j in i:
                images.append(j)
        paginator = Paginator(posts_list, 10)

        page = request.GET.get('page', 1)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        return render(request, 'feed/searchresults.html', {'posts': posts, 'images':images})

@login_required
def academics_posts(request):
    posts_list = Post.objects.filter(category__contains='AC')[:50]
    images = []
    for postobj in posts_list:
        i = Photo.objects.filter(post=postobj)
        for j in i:
            images.append(j)
    paginator = Paginator(posts_list, 10)

    page = request.GET.get('page', 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'feed/academics.html', {'posts': posts, 'images':images})

@login_required
def clubs_and_association_posts(request):
    posts_list = Post.objects.filter(category__contains='CA')[:50]
    images = []
    for postobj in posts_list:
        i = Photo.objects.filter(post=postobj)
        for j in i:
            images.append(j)
    paginator = Paginator(posts_list, 10)

    page = request.GET.get('page', 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'feed/clubsassociations.html', {'posts': posts, 'images':images})

@login_required
def sports_posts(request):
    posts_list = Post.objects.filter(category__contains='SP')[:50]
    images = []
    for postobj in posts_list:
        i = Photo.objects.filter(post=postobj)
        for j in i:
            images.append(j)
    paginator = Paginator(posts_list, 10)

    page = request.GET.get('page', 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'feed/sports.html', {'posts': posts, 'images':images })

@user_passes_test(check_if_faculty)
def add_material(request):
    if request.method == "POST":
        course_material = CourseMaterial()
        course_material.course = request.POST['course']
        course_material.category = request.POST['category']
        course_material.file = request.FILES['file']
        course_material.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def show_material(request):
    return render(request, 'feed/subjects.html')

@login_required
def view_assignments(request, course_id):
    assignments = CourseMaterial.objects.filter(course__pk=course_id, category='AS')
    print(assignments)
    return render(request, 'feed/assignments.html', {'assignments': assignments})

@login_required
def view_notes(request, course_id):
    notes = CourseMaterial.objects.filter(course__pk=course_id, category='NO')
    return render(request, 'feed/notes.html', {'notes': notes})

@login_required
def view_previous_papers(request, course_id):
    previous_papers = CourseMaterial.objects.filter(course__pk=course_id, category='PP')
    return render(request, 'feed/previous_papers.html', {'previous_papers': previous_papers})