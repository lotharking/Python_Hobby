from posts.models import Posts
from django.contrib import admin

class PostsAdmin(admin.ModelAdmin):
    """Posts admin"""
    
    list_display = (
        'user',
        'profile',
        'title',
        'photo',
    )
    
    readonly_fields = ('created', 'modified')

admin.site.register(Posts,PostsAdmin)
