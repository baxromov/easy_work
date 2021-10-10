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
