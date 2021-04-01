from django.shortcuts import render,redirect
from seller.models import Item
from django.http import HttpResponse
from django.contrib import messages
from .forms import FilterForm
# Create your views here.

# Fuction For buyItem
def buyItem(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=FilterForm(request.POST)
            if fm.is_valid():
                form=fm.cleaned_data
                query=form.get('query')
                location=form.get('location')
                min_price=int(form.get('min_price'))
                max_price=int(form.get('max_price'))

                if len(query)>75:
                    Items=Item.objects.none()
                else:
                    itemByName = Item.objects.filter(item_name__icontains=query)
                    itemByCategory = Item.objects.filter(category__icontains=query)
                    itemByDescr = Item.objects.filter(description__icontains=query)
                    itemByUnion = set(itemByName.union(itemByCategory,itemByDescr))
                    itemByFilter=set(Item.objects.filter(city=location,price__gte=min_price,price__lte=max_price))
                    Items=itemByFilter.intersection(itemByUnion)
                    
                    if len(itemByFilter)==0:
                        messages.warning(request, "No search results found for this filter.Please enter other filter credentials")
                        return redirect("/buyer/buyItem/")
                if len(Items)==0:
                    messages.warning(request, "No search results found. Please refine your query.")
                return render(request, 'buyer/result.html',{'items': Items, 'query': query})
            else:
                messages.warning(request,"Please enter valid filter credentials!")
                return redirect("/buyer/buyItem/")
        else:
            fm=FilterForm()
            return render(request,'buyer/buyItem.html',{'form':fm})
    else:
        messages.error(request,"To Buy Item Please Login!!!")
        return redirect('/')


#After click on view on item this function would be called

def show_item(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            item=Item.objects.get(pk=id)
            return render(request,'buyer/show_item_details.html',{'item':item})
        else:
            return render(request,'error404.html')
    else:
        return render(request,'error404.html')


        