from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm
from django.forms import fields


class SignupForm(forms.ModelForm):
    username = forms.CharField(label='Username',widget=forms.TextInput(
        attrs={
            'class':'form-control bg-light'
        }
    ))

    first_name = forms.CharField(label='First Name', widget=forms.TextInput(
        attrs={
            'class': 'form-control bg-light'
        }
    ))

    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(
        attrs={
            'class': 'form-control bg-light'
        }
    ))

    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={
            'class': 'form-control bg-light'
        }
    ))

    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control bg-light'
        }
    ))

    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control bg-light'
        }
    ))


    class Meta:
        model = User
        fields =['username', 'first_name', 'last_name', 'email', 'password']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError(
                "Password is too short. must be 8 chars")

        return password

    def clean_confirm_password(self):
        password = self.claened_data.get('password')
        confirm_password = self.cleanded_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password and Confirm Password does not match")

        return confirm_password


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={
            'class': 'form-control bg-light',
        }
    ))

    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control bg-light',
        }
    ))

    class Meta:
        model = User
        fields = ['username','password']
