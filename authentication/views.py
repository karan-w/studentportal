from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from feed.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

# Create your views here.

def signin(request):
    if request.user.is_authenticated==True and request.user.is_active == True :
        return redirect('/')
    if request.method == 'GET':
        return render(request, 'authentication/signin.html', None)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user == None :
            return render(request, 'authentication/signin.html', {'error' : 'Please check your credentials. The username or password you entered is invalid. Try again.'})
        elif user.is_active == False :
            return render(request, 'authentication/signin.html', {'error' : 'User is not active. Please contact admin.'})
        else :
            login(request, user)
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
                    
            return render(request, 'feed/feed.html', {'posts':posts})
  
def signout(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def change_password(request):
    if request.method == 'GET':
        return render(request, 'authentication/change_pass.html', {})
    else:
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']

        user = User.objects.get(username=request.user.username)
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            logout(request)
            return redirect('/')
        else:
            error = "Existing password is incorrect."
            return render(request, 'authentication/change_pass.html', {'error': error})