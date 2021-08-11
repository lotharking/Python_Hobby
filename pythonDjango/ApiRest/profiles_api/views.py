from django.http import response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication # Genera token ramdom para autenticacion
from rest_framework.authtoken.views import ObtainAuthToken 
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from profiles_api import serializers, models, permissions

class HelloApiView(APIView):
    """ Clase APIView prueba con sus tipos de metodos existentes para API's
    Usados cuando: 
    - Control logica
    - Proceso de archivos y renderizado de respuesta sincrona
    - Lamadas API's y servicios
    - Acceso a archivos locales o datos """

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ retornar lista de caracteristicas del APIView """
        an_apiview = [
            'Usamos metodos HTTP como funciones (get, post, patch, put, delete)',
            'Es similar a una vista tradicional de Django',
            'Nos da el mayor control sobre la logica de nuestra aplicacion',
            'Esta mapeando manualmente a los urls'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """ Crea un mensaje con nuestro nombre """
        serializer = self.serializer_class(data=request.data) # Clase que viene con el APIView que lo configura para su uso, es su manera estandar para un view basado en clases de api

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message':message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """ Maneja actualizacion de un objeto, para actualizar objeto se le pide ID
         pero como en este caso no se trabajara con ID se define el 'pk=None' """
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """ Maneja actualizacion parcial de un objeto """
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """ Maneja eliminacion de un objeto """
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """ ViewSet de prueba, usado para editar objetos en especifico y
    es por ello que es el mas comun en las DB """

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ Retornar mensaje en hola mundo """

        a_viewset = [
            'usa acciones (list, create, update, partial_update)',
            'Automaticamente mapea a los URLs usando Routers',
            'Proveee mas funcionalidades con menos codigo'
        ]

        return Response({'message': 'Hola', 'a_viewset': a_viewset})

    def create(self, request):
        """ Crear nuevo mensaje de Hola Mundo """

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hola {name}"
            return Response({'message':message})
        else:
            return Response(
                serializer.errors, 
                status = status.HTTP_400_BAD_REQUEST
                )

    def retrieve(self, request, pk=None):
        """ Obtiene un objeto y su ID """

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """ Actualiza un objeto """

        return Response({'http_method': 'PUT'})

    def parcial_update(self, request, pk=None):
        """ Actualiza un objeto con informacion parcial """

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """ Destruye un objeto """

        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """ Crear y actualizar perfiles """

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all() # Llama a los objetos y evita definir nombre en el url
    authentication_classes = (TokenAuthentication, ) # Como el usuario se autentica
    permission_classes = (permissions.UpdateOwnProfile, ) # Que permisos tiene el usuario
    filter_backends = (filters.SearchFilter, ) # Filtros de busquedade usuarios
    search_fields = ('name', 'email',) # Como se quiere buscar

class UserLoginApiView(ObtainAuthToken):
    """ Se encargara de crear los tokens de autenticacion del usuario """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES # Agrega las clases de renderer al token de autenticacion

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """ Maneja el crear, leer y actualizar el profile feed """
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItemm.objects.all() # Ordenar todos los items que contenga
    permission_classes = (
        permissions.UpdateOwnStatus, 
        IsAuthenticated # IsAuthenticatedOrReadOnly -> usuarios no autenticados pueden leer el api, IsAuthenticated -> solo autenticados
        ) # Agregamos nuestros permisos personalizados

    def perform_create(self, serializer):
        """ Se encarga de setear el perfil de usuario para el usuario que esta loggeado """
        serializer.save(user_profile=self.request.user)