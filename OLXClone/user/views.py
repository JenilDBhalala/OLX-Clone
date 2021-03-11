from django.shortcuts import render,redirect
from django.http import HttpResponse
from django import forms
from django.contrib import messages
from seller.models import Item
from seller.forms import AddItemForm
# Create your views here.

def your_products(request):
    usr_id=request.user.id
    items=Item.objects.filter(seller_id=usr_id)
    print("before render")
    return render(request,'user/your_products.html',{'items':items})


def edit_item(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            print("this is inside post")
            itm=Item.objects.get(pk=id)
            fm=AddItemForm(request.POST,request.FILES,instance=itm)
            if fm.is_valid():
                fm.save()
                messages.success(request, "item details updated succesfully")
            else:
                messages.error(request, "item details not updated")
            return redirect('/user/your_products/')
        else:
            itm=Item.objects.get(pk=id)
            fm=AddItemForm(instance=itm)
            fm.fields['seller_id'].widget=forms.HiddenInput()
            return render(request,'user/edit_item.html',{'form':fm})
    else:
        return HttpResponse("404- Not Found")


def delete_item(request,id):
    if request.user.is_authenticated:
        itm=Item.objects.get(pk=id)
        itm.delete()
        messages.success(request, "item deleted succesfully")
        # itm=Item.objects.get(pk=id))
        return redirect('/user/your_products/')
    else:
        return HttpResponse("404- Not Found")


