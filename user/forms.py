from typing import Any
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import Profile
# from user.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class Signup(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'username' }))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder' : 'email' }))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'password', }))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'confirm password', }))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =  ['bio', 'date_of_birth', 'phone', 'city', 'image']

