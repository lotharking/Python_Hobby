from django.contrib.auth import get_user_model, authenticate
from django.db import models
from django.utils.translation import ugettext_lazy as _ # Traductor de token

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """ Serializador para el objeto de usuarios """

    class Meta:
        model = get_user_model()
        """ Estos son los datos que se convierten en json cuando se haga la peticion """
        fields = ('email', 'password', 'name')
        extra_kwargs = {'password':{'write_only':True, 'min_length':5}}

    def create(self, validated_data):
        """ Crear nuevo usuario con clave encryptada """
        return get_user_model().objects.create_user(**validated_data)

class AuthTokenSerializer(serializers.Serializer):
    """ Serializador para el objeto de autentificacion del usuario """
    email = serializers.CharField()
    password = serializers.CharField(
        style = {'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs): # attrs es cualquier campo que conforma nuestro serializador
        """ Validar y autenticar el usuario """
        email=attrs.get('email')
        password=attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username = email,
            password=password
        )

        if not user:
            msg=_('unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg,code='authorization')

        attrs['user'] = user

        return attrs