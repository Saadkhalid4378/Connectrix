from django import forms
from .models import Thought, Comment

class ThoughtForm(forms.ModelForm):
    class Meta:
        model = Thought
        fields = ['title', 'text', 'image', 'is_private']  


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['text']