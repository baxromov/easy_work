from django import forms


class Login(forms.Form):
    username = forms.CharField(max_length=16, required=True)
    password = forms.CharField(max_length=16, required=True)
