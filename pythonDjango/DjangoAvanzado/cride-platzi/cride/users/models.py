"""Users model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utilities
from cride.utils.models import CRideModel

class User(CRideModel, AbstractUser):
    """User model.
    Extend from Django's Abstract User, change the username field
    to email and add some extra fields.
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with thatemail already exists'
        }
    )

    phone_nomber = models.CharField(max_length=17,blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'client status',
        default=True,
        help_text=(
            'Help easily distinguish users and perform queries.'
            'Client are the main type of users'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=False,
        help_text= 'Set the true when the user have verified its email address.'
    )