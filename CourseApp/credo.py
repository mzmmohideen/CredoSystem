from django import forms


class InputForm(forms.Form):
    first_name = forms.CharField(label= "Enter First Name", max_length=200, required=False)
    last_name = forms.CharField(max_length=200)
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget= forms.PasswordInput())