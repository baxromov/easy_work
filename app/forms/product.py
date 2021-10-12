from django import forms

from app.models import product


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = product.Product
        fields = (
            'name',
            'category',
            'measurement',
            'price',
            'quantity',
            'image',
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'category': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'measurement': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
            'image': forms.FileInput(attrs={'id': 'myDropify'}),
        }
