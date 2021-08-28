""" Posts models """

# Django
from django.db import models

class User(models.Model):
    """ User model """
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    country = models.CharField(max_length=100, null=True,default='null')
    city = models.CharField(max_length=100, null=True,default='null')

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_admin = models.BooleanField(default=False)

    bio = models.TextField(blank=True)

    birthdate = models.DateField(blank=True, null=True)

    create = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email