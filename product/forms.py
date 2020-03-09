from .models import Product
from django import forms


class Form1(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('price', 'price')
