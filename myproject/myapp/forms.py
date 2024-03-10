from django import forms
from django.contrib.auth.models import User

from .models import Blog


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['username', 'title', 'content']