from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'purchase_status', 'purchase_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'purchase_status': forms.CheckboxInput(attrs={'class': 'form-check'}),
            'purchase_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
