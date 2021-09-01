from django import forms
from .models import *


class SellingForm(forms.ModelForm):
    class Meta:
        model = SpareParts
        fields = ['ad', 'marka', 'sheher', 'shekil', 'qiymet', 'mezenne', 'info']
        shekil = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
