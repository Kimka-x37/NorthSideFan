from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class Register_form(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'input',
            'placeholder': 'Введiть нiк...'
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input',
            'placeholder': 'Введiть пароль...'
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input',
            'placeholder': 'Повторiть пароль...'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class Login_form(forms.Form):
    username = forms.CharField(max_length=15,
        widget=forms.TextInput(attrs={
            'class': 'input',
            'placeholder': 'Введiть нiк...'
    }))
    password = forms.CharField(max_length=150,
        widget=forms.PasswordInput(attrs={
            'class': 'input',
            'placeholder': 'Введiть пароль...'
    }))
