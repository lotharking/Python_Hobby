"""Platzi url module"""

# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from platzigram import view as local_view
from posts import views as posts_views
from user import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-word/', local_view.hello_word, name='hello_word'),
    path('sorted/', local_view.sorted, name= 'sort'),
    path('hi/<str:name>/<int:age>/', local_view.say_hi, name='hi'),

    path('posts/', posts_views.list_posts, name='feed'),

    path('users/login/', users_views.login_view, name='login'),
    path('users/logout/', users_views.logout_view, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
