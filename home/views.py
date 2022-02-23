from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.core import validators


# Create your views here.

def index(request):
    if request.method== 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        return redirect('/')
            
    return  render(request, 'index.html')

