"""Forms users"""

# Django
from django import forms

# Models
from django.contrib.auth.models import User

class SignupForm(forms.Form):
    """Signup form"""
    username = forms.CharField(min_length=4, max_length=50)
    password = forms.CharField(
        max_length=70, 
        widget=forms.PasswordInput()
        )
    password_confirmation = forms.CharField(
        max_length=70, 
        widget=forms.PasswordInput()
        )
    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)
    email = forms.CharField(
        min_length=6, 
        max_length=70, 
        widget=forms.EmailInput()
        )

    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exist()
        if username_taken:
            raise forms.ValidationError('username is already in use')
        return username

    def clean(self):
        """Verify password confirmation match"""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            forms.ValidationError('password do no match')

        return data

class ProfileForm(forms.Form):
    """Forms profile for user"""

    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()