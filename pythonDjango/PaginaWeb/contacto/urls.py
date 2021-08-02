from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Contacto, name="Contacto"), # El path esta vacio porque esta en la misma carpeta de la vista
    # path('categoria/<int:categoria_id>/', views.Contacto, name="Contacto"), 
]
