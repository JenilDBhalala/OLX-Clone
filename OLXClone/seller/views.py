from django.shortcuts import render,redirect
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import AddItemForm
from django import forms
from .models import Item
# Create your views here.

#This Function will add item to database 
def addItem(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=AddItemForm(request.POST,request.FILES)
            if fm.is_valid():
                fm.save()
                messages.success(request,"Item added Successfully")
                item1=Item.objects.latest('id')
                return render(request,'seller/show_item.html',{'item':item1})
            else:
                messages.error(request,"form is invalid - Please Fill up correctly")
                return redirect("/seller/addItem/")
        else:
            usr_id=request.user.id
            fm=AddItemForm()
            fm.initial['seller_id']=usr_id
            fm.fields['seller_id'].widget=forms.HiddenInput()
            return render(request,'seller/addItem.html',{'form':fm})
    else:
        messages.error(request,"To sell Item Please Login!!!")
        return redirect('/')

#fuction for edit item details
def edit_item(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            itm=Item.objects.get(pk=id)
            fm=AddItemForm(request.POST,request.FILES,instance=itm)
            if fm.is_valid():
                fm.save()
                messages.success(request, "Item details updated succesfully")
            else:
                messages.error(request, "Item details not updated")
            return redirect('/user/my_products/')
        else:
            itm=Item.objects.get(pk=id)
            fm=AddItemForm(instance=itm)
            fm.fields['seller_id'].widget=forms.HiddenInput()
            return render(request,'seller/edit_item.html',{'form':fm})
    else:
        return render(request,'error404.html')

#This function will delete the Item from database
def delete_item(request,id):
    if request.user.is_authenticated:
        itm=Item.objects.get(pk=id)
        itm.delete()
        messages.success(request, "Item deleted succesfully")
        return redirect('/user/my_products/')
    else:
        return render(request,'error404.html')