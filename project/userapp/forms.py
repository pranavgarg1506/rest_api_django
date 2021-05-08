from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . import models


class NewUserForm(forms.Form):

    name = forms.CharField(label = 'Name', required = True)
    email = forms.EmailField(label = 'Email', required = True)
    contact = forms.CharField(label = 'Contact', required = True)
    username = forms.CharField(label = 'Username', required = True)
    password1 = forms.CharField(label = 'Password', required = True, widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Password (Again)', required = True, widget = forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()

        passw1 = cleaned_data['password1']
        passw2 = cleaned_data['password2'] 


        if len(passw1) < 8:
            raise forms.ValidationError('Password should be 8 or more than 8 chararcters')
        if passw1 != passw2:
            raise forms.ValidationError("Passwords do not match")

class LoginUserForm(forms.Form):

    username = forms.CharField(label = 'Uusername')
    password = forms.CharField(label = 'Password', required = True, widget = forms.PasswordInput)