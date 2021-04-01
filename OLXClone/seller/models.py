from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Item(models.Model):
    category=models.CharField(max_length=20)
    item_name=models.CharField(max_length=30)
    price=models.PositiveIntegerField() 
    model_year=models.CharField(max_length=4)
    city=models.CharField(max_length=15)
    area=models.CharField(max_length=20)
    photo=models.ImageField(upload_to="itemImage")
    description=models.TextField()
    seller_id=models.ForeignKey(User,on_delete=models.CASCADE)
    mo_no=models.CharField(max_length=10)
    date=models.DateTimeField(auto_now=True)  