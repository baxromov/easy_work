from django import forms

from app.models import category


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = category.Category
        exclude = ('user',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
