from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import Profile
# from user.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class Signup(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =  ['user', 'bio', 'date_of_birth', 'phone', 'city', 'image']

