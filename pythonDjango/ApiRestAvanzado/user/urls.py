from django.urls import path

from user import views

app_name = 'user' # Se define el url para la app llamada aqui

urlpatterns = [ 
    path('create/', views.CreateUserView.as_view(), name = 'create'), # como es una clase se le coloca el as_view para poder verlo
    path('token/', views.CreateTokenView.as_view(), name = 'token'),
    path('me/', views.ManageUserView.as_view(), name = 'me'),
]