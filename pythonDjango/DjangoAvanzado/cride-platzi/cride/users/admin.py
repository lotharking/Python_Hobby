"""User models admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from cride.users.models import User,Profile

class CustomUserAdmin(UserAdmin):
    """User model admin."""
    
    list_display = ('email', 'username', 'firs_name', 'last_name', 'is_staff', 'is_client')
    list_filter = ('is_client', 'is_staff', 'created', 'modified')

admin.site.register(User, CustomUserAdmin)