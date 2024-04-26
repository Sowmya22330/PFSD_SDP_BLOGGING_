from django import forms
from django.contrib.auth.models import User

from .models import Blog, Rating



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['username', 'title', 'content']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating', 'comments']
        widgets = {
            'rating': forms.RadioSelect(),
            'comments': forms.Textarea(attrs={'rows': 6}),
        }
