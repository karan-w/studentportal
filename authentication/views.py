from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def signin(request):
    if request.user.is_authenticated==True and request.user.is_active == True :
        return redirect('/')
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = user_name, password = password)
        if user == None :
            return render(request, 'authentication/signin.html', {'error' : 'Please check your credentials. The username or password you entered is invalid. Try again.'})
        elif user.is_active == False :
            return render(request, 'authentication/signin.html', {'error' : 'User is not active. Please contact admin.'})
        else :
            login(request, user)
    return render(request, 'authentication/signin.html', None)