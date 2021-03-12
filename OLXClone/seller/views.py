from django.shortcuts import render,redirect
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import AddItemForm
from django import forms
from .models import Item
from django.contrib import messages
# Create your views here.

def addItem(request):
    if request.method=='POST':
        fm=AddItemForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            item1=Item.objects.latest('id')
            # item1=Item.objects.all()
            messages.success(request, "Item added successfully!")
            return render(request,'show_item.html',{'item':item1})
    else:
        usr_id=request.user.id
        fm=AddItemForm()
        fm.initial['seller_id']=usr_id
        fm.fields['seller_id'].widget=forms.HiddenInput()  
        return render(request,'addItem.html',{'form':fm})
