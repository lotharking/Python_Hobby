"""Platzi url module"""

# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from platzigram import view as local_view
from posts import views as posts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-word/', local_view.hello_word),
    path('sorted/', local_view.sorted),
    path('hi/<str:name>/<int:age>/', local_view.say_hi),

    path('posts/', posts_views.list_posts),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
