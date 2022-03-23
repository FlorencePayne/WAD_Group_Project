from django import forms
from floppa.models import Necklace

class NecklaceForm(forms.ModelForm):
    name = forms.CharField(max_length=20, help_text="Please enter the necklace name!")
    colour = forms.CharField(max_length=10)
    description = forms.CharField(max_length=50)
    price = forms.CharField(max_length=4)
    stock = forms.IntegerField(initial=0)

    # inline class to provide additional information for the form
    class Meta:
        # provide association betwen ModelForm and a model
        model = Necklace
        exclude = ('slug', 'image1', 'image2',)