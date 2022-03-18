from django.db.models import fields
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django import forms
class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields='__all__'
      



class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=('id','name','phone','email')
       
class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields='__all__'
      
    
        
        