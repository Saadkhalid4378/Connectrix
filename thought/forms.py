from django import forms
from .models import Thought, Comment

class ThoughtForm(forms.ModelForm):
    class Meta:
        model = Thought
        fields = ['title', 'image', 'is_private']  


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['text']