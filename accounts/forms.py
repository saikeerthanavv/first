from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100,required=False)
    class Meta:
        model = User
        fields =(
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2',
            )
