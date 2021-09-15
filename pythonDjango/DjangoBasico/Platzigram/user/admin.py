"""User admin class"""

# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models
from django.contrib.auth.models import User
from user.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ Profile admin """

    list_display = ('pk','user','phone_number','website', 'picture', 'posts_count')
    list_display_links = ('pk','user')
    list_editable = ('phone_number', 'website', 'picture')
    search_fields = (
        'user__email', 
        'user__username', 
        'user__first_name'
        , 'user__last_name'
        , 'phone_number'
        )

    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created', 
        'modified',
        )

    fieldsets = (
        ('Profile', {
            'fields':(('user', 'picture'),
                    ('posts_count'),),
        }),
        ('Extra info', {
            'fields':(('website', 'phone_number'),
                    ('biography'),),
        }),
        ('Metadata', {
            'fields':('created', 'modified',),
        }),
    )

    readonly_fields = ('created', 'modified')

class ProfileInline(admin.StackedInline):
    """Profile admin in-line for user"""

    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'

class UserAdmin(BaseUserAdmin):
    """Add profile admin to BaseUserAdmin"""

    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)