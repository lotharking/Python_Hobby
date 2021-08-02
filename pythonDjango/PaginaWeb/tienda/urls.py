from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.tienda, name="Tienda"), # El path esta vacio porque esta en la misma carpeta de la vista
]
