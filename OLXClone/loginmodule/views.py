from django.shortcuts import render,redirect
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
# Create your views here.


def login(request):
    if request.method=='POST':
        username1=request.POST['username']
        password1=request.POST['password']
        user=auth.authenticate(username=username1,password=password1)
        if user is not None:
            auth.login(request,user)
            return redirect('/loginmodule/role/')
        else:
            return redirect("/loginmodule/login/")
            # return HttpResponseRedirect('/login/please')
    else:
        return render(request,'login.html')


def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email=request.POST['email_id']
        password=request.POST['password']

        x=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
        x.save()
        print("user created")
        return redirect('/loginmodule/login/')
    else:
        return render(request,'signup.html')


def role(request):
    if request.method=='POST':
        if 'buyer' in request.POST:
            return HttpResponseRedirect("/buyer/buyItem/")
        elif 'seller' in request.POST:
            return HttpResponseRedirect("/seller/addItem/")
        else:
            print("error")

    else:
        return render(request,'role.html')