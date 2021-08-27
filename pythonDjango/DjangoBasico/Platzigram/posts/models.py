""" Posts models """

# Django
from django.db import models

class User(models.Model):
    """ User model """
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    bio = models.TextField()

    birthdate = models.DateField(blank=True, null=True)

    create = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)