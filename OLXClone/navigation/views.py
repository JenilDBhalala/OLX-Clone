from django.shortcuts import render, redirect
from django.http import HttpResponse
from navigation.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User 
import re
from django.contrib.auth  import authenticate,  login, logout
from seller.models import Item
# Create your views here.

def home(request):
    itms=Item.objects.all()
    return render(request, 'home/home.html',{'items':itms})

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            name=request.POST['name']
            email=request.POST['email']
            phone=request.POST['phone']
            content=request.POST['content']
            if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
                messages.error(request, "Please fill the form correctly")
            else:
                contact=Contact(name=name, email=email, phone=phone, content=content)
                contact.save()
                messages.success(request, "Your message has been sent successfully")
        return render(request, "home/contact.html")
    else:
        return HttpResponse("404 - Not Found")

def help(request):
    return render(request, 'home/help.html')

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username)>15:
            messages.error(request, " Username must be under 15 characters")
            return redirect('/')

        if not username.isalnum():
            messages.error(request, " Username must be contain letters and numbers")
            return redirect('/')

        if pass1!= pass2:
            messages.error(request, " Passwords didn't match")
            return redirect('/')

        if len(pass1)<6:
            messages.error(request, " Your password must be atleast 6 characters")
            return redirect('/')

        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if not re.search(regex,email): 
            messages.error(request, " Provided e-mail is Invalid")
            return redirect('/') 


        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your account has been created successfully")
        return redirect('/')

    else:
        return HttpResponse("404 - Not found")

def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In!")
            return redirect("/")
        else:
            messages.error(request, "Invalid credentials! Please try again!")
            return redirect("/")

    return HttpResponse("404- Not Found")

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged out!")
    return redirect('/')
# def search(request):
#     return HttpResponse("We are at search")

# def productview(request):
#     return HttpResponse("We are at productview")

# def checkout(request):
#     return HttpResponse("We are at checkout")