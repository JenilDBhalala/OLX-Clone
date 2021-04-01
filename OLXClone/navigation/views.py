from django.shortcuts import render, redirect
from django.http import HttpResponse
from navigation.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User 
import re
from django.contrib.auth  import authenticate,  login, logout
from seller.models import Item
# Create your views here.

#function for showing Home page 
def home(request):
    itms=reversed(Item.objects.all())
    print(itms)
    return render(request, 'home/home.html',{'items':itms})

#For about page
def about(request):
    return render(request, 'home/about.html')

#For contact to admin 
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
        messages.error(request,"For Contact Please Login!!!")
        return redirect("/")

#for SingUP

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
        return render(request,'error404.html')

#This function check authentication for user 
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

    return render(request,'error404.html')

#for logout
def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged out!")
    return redirect('/')

#function would be called for search item on navigation bar 
def search(request):
    query=str(request.GET['query'])
    if query is not "":
        if len(query)>75 and len(query)<1:
            Items=set()
        else:
            split_query=query.split()
            Items=set(Item.objects.all())
            for q in split_query:
                item1=Item.objects.filter(item_name__icontains=q)
                item2 = Item.objects.filter(city__icontains=q)
                item3 = Item.objects.filter(description__icontains=q)
                item4 = Item.objects.filter(category__icontains=q)
                item=set(item1.union(item2,item3,item4))
                Items=Items & item
        if len(Items)==0:
            messages.warning(request, "No search results found. Please refine your query.")
        params={'items': Items, 'query': query}
        return render(request, 'home/search.html', params)
    else:
        return redirect("/")


