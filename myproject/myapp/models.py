# Assuming your Django app is named 'blog'

# In your models.py file

from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=150)

    def _str_(self):
        return self.username