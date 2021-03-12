from django.shortcuts import render,redirect
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import AddItemForm
from django import forms
from .models import Item
# Create your views here.

def addItem(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=AddItemForm(request.POST,request.FILES)
            if fm.is_valid():
                fm.save()
                item1=Item.objects.latest('id')
                return render(request,'show_item.html',{'item':item1})
            else:
                messages.error(request,"form is invalid - Please Fill up correctly")
                return redirect("/seller/addItem/")
        else:
            usr_id=request.user.id
            fm=AddItemForm()
            fm.initial['seller_id']=usr_id
            fm.fields['seller_id'].widget=forms.HiddenInput()
            return render(request,'addItem.html',{'form':fm})
    else:
        messages.error(request,"To sell Item Please Login!!!")
        return redirect('/')

