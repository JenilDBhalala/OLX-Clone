from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class FilterForm(forms.Form):
    CITY_CHOICES=[('surat','Surat'),('vadodara','Vadodara'),('ahmedabad','Ahmedabad'),
                      ('gandhinagar','Gandhinagar'),('junagadh','Junagadh'),('bharuch','Bharuch'),
                      ('bhavanagar','Bhavanagar'),('jamanagar','Jamanagar'),('anand','Anand'),
                      ('nadiad','Nadiad'),('mahesana','Mahesana'),('amreli','Amreli'),
                      ('kutch','Kutch'),('patan','Patan'),('navsari','Navsari'),('botad','Botad'),
                      ('dwarka','Dwarka'),('valsad','Valsad'),('morabi','Morabi'),('surendranager','Surendranagar')]

    query=forms.CharField(max_length=20,label="",widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Search item'}))
    location=forms.ChoiceField(choices=CITY_CHOICES,widget=forms.Select(attrs={'class' :'form-control'}))
    min_price=forms.IntegerField(label="Budget : Min To Max",widget=forms.NumberInput(attrs={'class': 'form-control'}))
    max_price=forms.IntegerField(label="To",label_suffix="",widget=forms.NumberInput(attrs={'class': 'form-control'}))
    