from cmath import log
from tkinter import E
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
from .models import Profile

# Create your views here.

def login_page(request):
    return render(request, 'accounts/login.html')

def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)

        if user_obj.exists():
            messages.error(request, 'Youser already registered')
            return HttpResponseRedirect(request.path_info)
        print(email)
        user = User.objects.create_user(first_name = first_name, last_name = last_name, username = email)
        user.set_password(password)
        user.save()
        messages.success(request, 'An email has been sent on your mail.')


    return render(request, 'accounts/register.html')