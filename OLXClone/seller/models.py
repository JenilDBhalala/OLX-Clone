from django.db import models

# Create your models here.



class Item(models.Model):
    item_name=models.CharField(max_length=20)
    prize=models.IntegerField()
    model_year=models.CharField(max_length=4)
    city=models.CharField(max_length=10)
    photo=models.ImageField(upload_to="itemImage")
    description=models.TextField()
    seller_id=models.IntegerField()
    mo_no=models.CharField(max_length=10)
    date=models.DateTimeField(auto_now=True)  