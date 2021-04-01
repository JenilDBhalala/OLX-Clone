from django import forms
from django.contrib.auth.models import User

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password']
        labels={'first_name':'First Name','last_name':'Last Name'}

        widgets={'username':forms.TextInput(attrs={'class' : 'form-control'}),
                'email':forms.EmailInput(attrs={'class' : 'form-control'}),
                'first_name':forms.TextInput(attrs={'class' : 'form-control'}),
                'last_name':forms.TextInput(attrs={'class' : 'form-control'}),
                'password':forms.PasswordInput(render_value=True ,attrs={'class' : 'form-control'}),}

    