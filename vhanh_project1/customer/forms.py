from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Customer
from django import forms

class LoginForm(AuthenticationForm):
    class Meta:
        model = Customer
        fields = ["username", "password"]

class RegisterForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ["username", "email", "password1", "password2"]


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['username', 'email', 'bio', 'customer_type']
