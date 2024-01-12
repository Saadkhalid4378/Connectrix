from django import forms
from .models import Thought

class ThoughtForm(forms.ModelForm):
    class Meta:
        model = Thought
        fields = ['title', 'image', 'is_private']  
