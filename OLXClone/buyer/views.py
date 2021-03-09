from django.shortcuts import render
from seller.models import Item
# Create your views here.

def buyItem(request):
    return render(request,'buyItem.html')


def result(request):
    if request.method=='POST':
        name=request.POST['item_name']
        city=request.POST['city']
        # print(name)
        # print(city)
        items=Item.objects.filter(item_name=name,city=city)
        print(items)
        return render(request,'result.html',{'items':items})


def show_item(request,id):
    if request.method=='POST':
        item=Item.objects.get(pk=id)
        return render(request,'show_item_details.html',{'item':item})