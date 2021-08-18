from django.core.exceptions import ImproperlyConfigured
from rest_framework import generics

from user.serializers import UserSerializer, AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.settings import api_settings

class CreateUserView(generics.CreateAPIView):
    """ Crear nuevo usuario en el sistema """
    serializer_class = UserSerializer

class CreateTokenView(ObtainAuthToken):
    """ Crear un nuevo auth token para usuario """
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES # Permite que se pueda observar en cualquier navegador