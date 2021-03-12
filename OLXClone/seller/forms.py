from django import forms
from .models import Item

class AddItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields='__all__'
        labels={'photo':'Image','mo_no':'Mobile Number'}
        CITY_CHOICES=[('surat','Surat'),('vadodara','Vadodara'),('ahmedabad','Ahmedabad'),
                      ('gandhinagar','Gandhinagar'),('junagadh','Junagadh'),('bharuch','Bharuch'),
                      ('bhavanagar','Bhavanagar'),('jamanagar','Jamanagar'),('anand','Anand'),
                      ('nadiad','Nadiad'),('mahesana','Mahesana'),('amreli','Amreli'),
                      ('kutch','Kutch'),('patan','Patan'),('navsari','Navsari'),('botad','Botad'),
                      ('dwarka','Dwarka'),('valsad','Valsad'),('morabi','Morabi'),('surendranager','Surendranagar'),
                     ]
        CATEGORY_CHOICES=[('bike','Bike'),('car','Car'),('scooter','Scooter'),
                        ('laptop','Laptop'),('mobile','Mobile'),('tablet','Tablet'),('tv','TV')]

        widgets={'category':forms.Select(choices=CATEGORY_CHOICES,attrs={'class' : 'form-control'}),
                'item_name':forms.TextInput(attrs={'class' : 'form-control'}),
                'price':forms.NumberInput(attrs={'class' : 'form-control'}),
                'model_year':forms.TextInput(attrs={'class' : 'form-control'}),
                'city':forms.Select(choices=CITY_CHOICES,attrs={'class' : 'form-control'}),
                'area':forms.TextInput(attrs={'class' : 'form-control'}),
                'description':forms.Textarea(attrs={'class' : 'form-control'}),
                'mo_no':forms.TextInput(attrs={'class' : 'form-control'})}

    