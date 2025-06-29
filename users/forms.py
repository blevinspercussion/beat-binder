from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password']

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email')
    
    