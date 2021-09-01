from django import forms
from .models import Car, PostImage


class SellingForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'city', 'engine', 'body_type', 'transmission', 'milage', 'color', 'fueltype',
                  'year', 'power', 'price', 'currencie', 'credit', 'supply', 'info']



class Photos(forms.ModelForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    class Meta:
        model = PostImage
        fields = ['images']
