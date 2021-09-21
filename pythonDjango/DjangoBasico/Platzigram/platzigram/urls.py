"""Platzi url module"""

# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(('posts.urls', 'posts'), namespace='posts')),

    path('users/', include(('user.urls', 'user'), namespace='users')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
