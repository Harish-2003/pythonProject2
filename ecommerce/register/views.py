from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
# Create your views here.
from django.contrib import messages
def loginpage(r):
    return render(r,'login.html')
def register(r):
    if r.method=='POST':
        username=r.POST['username']
        first_name=r.POST['firstname']
        last_name=r.POST['lastname']
        email=r.POST['email']
        password=r.POST['pwd']
        user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
        user.save()
        return redirect('/')
    return render(r,'register.html')
def checker(r):
    if r.method=='POST':
        username=r.POST['username']
        pwd=r.POST['pwd']
        user=auth.authenticate(username=username,password=pwd)
        if user is not None:
            auth.login(r,user)
            return redirect('/home')
        else:
            messages.info(r,'invlaid credatinals')
            return redirect('/')
