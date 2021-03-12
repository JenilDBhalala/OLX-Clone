from django.contrib import admin
from .models import Item
# Register your models here.

@admin.register(Item)

class ItemAdmin(admin.ModelAdmin):
    list_display=['id','category','item_name','price','model_year','area','city']