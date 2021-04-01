from django.shortcuts import render,redirect
from django.http import HttpResponse
from django import forms
from django.contrib import messages
from seller.models import Item
from seller.forms import AddItemForm
from .forms import UpdateProfileForm

# Create your views here.

#This function shows list of product which entered by user
def my_products(request):
    if request.user.is_authenticated:
        usr_id=request.user.id
        items=Item.objects.filter(seller_id=usr_id)
        return render(request,'user/my_products.html',{'items':items})
    else:
        return render(request,'error404.html')

#For upadate profile 
def updateProfile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=UpdateProfileForm(request.POST,instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request,"Profile Modification Done")
                return redirect('/')
            else:
                messages.success(request,"Profile Modification Done")
                return redirect('/user/profile/update/')
        else:
            fm=UpdateProfileForm(instance=request.user)
            return render(request,'user/updateProfile.html',{'form':fm})
    else:
        return render(request,'error404.html')
