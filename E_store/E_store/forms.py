
from posixpath import split
from django import forms
from  django.contrib.auth.forms import UserChangeForm, UserCreationForm
from  django.contrib.auth.models import User
from store_app.models import Address
from django.core import validators

class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']
        labels = {'email': 'Email'}
       
        
class EditAddForm(forms.ModelForm):
      
    class Meta:
        model = Address
        
        fields = ["address","town_city","state","postcode","phone"]