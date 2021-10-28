"""Circles admin."""

# Django
from django.contrib import admin

# Model
from cride.circles.models import Circle

@admin.register(Circle)
class CirlceAdmin(admin.ModelAdmin):
    """Circle Admin."""

    list_display = (
        'slug_name',
        'name',
        'is_public',
        'is_verified',
        'is_limited',
        'members_limit',
    )

    search_fields = (
        'slug_name',
        'name',
    )

    list_filter = (
        'is_public',
        'is_verified',
        'is_limited',
    )