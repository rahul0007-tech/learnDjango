from django import forms

class RgistarionForm(forms.Form):
    username = forms.CharField( max_length=30, required=True)
    firstName = forms.CharField( max_length=30)
    lastName = forms.CharField( max_length=30)
    email = forms.EmailField(max_length=30, required=True)
    password = forms.CharField(max_length=20, required=True)