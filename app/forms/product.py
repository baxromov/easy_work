from django import forms
from app.models import product


class ProductModelForm(forms.Form):
    name = forms.CharField(max_length=255, required=True)
    category = forms.CharField(max_length=255, required=True)
    measurement = forms.CharField(max_length=255, required=True)
    price = forms.FloatField(required=True)
    quantity = forms.IntegerField(required=True)
    image = forms.FileField(required=False)

    def save(self):
        name = self.cleaned_data['name']
        category = self.cleaned_data['category']
        measurement = self.cleaned_data['measurement']
        price = self.cleaned_data['price']
        quantity = self.cleaned_data['quantity']
        image = self.cleaned_data['image']

        product.Product.objects.create(name=name,
                                       category=category,
                                       measurement=measurement,
                                       price=price,
                                       quantity=quantity,
                                       image=image
                                       )

