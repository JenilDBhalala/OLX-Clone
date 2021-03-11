from django import forms
from .models import Item

class AddItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields='__all__'
        labels={'photo':'Image','mo_no':'Mobile Number'}
        widgets={'item_name':forms.TextInput(attrs={'class' : 'form-control'}),
                'prize':forms.NumberInput(attrs={'class' : 'form-control'}),
                'model_year':forms.TextInput(attrs={'class' : 'form-control'}),
                'city':forms.TextInput(attrs={'class' : 'form-control'}),
                'description':forms.Textarea(attrs={'class' : 'form-control'}),
                'mo_no':forms.TextInput(attrs={'class' : 'form-control'})}

    