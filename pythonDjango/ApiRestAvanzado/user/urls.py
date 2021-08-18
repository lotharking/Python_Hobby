from django.urls import path

from user import views

app_name = 'user' # Se define el url para la app llamada aqui

urlpatterns = [ 
    path('create/', views.CreateUserView.as_view(), name = 'create') # como es una clase se le coloca el as_view para poder verlo
]