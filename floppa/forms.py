from django import forms
from floppa.models import Necklace, Customer
from django.contrib.auth.models import User


class NecklaceForm(forms.ModelForm):
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