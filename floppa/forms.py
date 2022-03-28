from unicodedata import name
from django import forms
from floppa.models import Necklace, Customer, Order_Necklace
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# main class to create form with parameter referencing the model which has already been created
class NecklaceForm(forms.ModelForm):
    # define the fields of the form
    name = forms.CharField(max_length=20)
    colour = forms.CharField(max_length=10)
    description = forms.CharField(max_length=50)
    price = forms.CharField(max_length=4)
    stock = forms.IntegerField(initial=0)

    # inline class to provide additional information for the form
    class Meta:
        # provide association betwen ModelForm and a model
        model = Necklace
        exclude = ('slug', 'image1', 'image2',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('address1', 'address2', 'postcode',)


class AddToCartForm(forms.ModelForm):
    quantity = forms.IntegerField(initial=1, min_value=1, max_value=3)
    
    class Meta:
        model = Order_Necklace
        fields = ('quantity',)
    