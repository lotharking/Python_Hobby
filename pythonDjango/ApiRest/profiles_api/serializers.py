""" Se usa para convertir informacion json, a traves de el se agrega el input, post, update, etc. 
Para poder recibir el contenido que se esta posteando al api """

from django.db.models import fields
from rest_framework import serializers

from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """ Serializa un campo para probar nuestro APIView """
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializa el perfil de un usuario """

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = { # Argumentos para proteger las claves de seguridad
            'password':{
                'write_only': True, # Solo se pueda mostrar cuando se esta creando
                'style':{'input_type': 'password'} # Mostrar los asteriscos y no datos (darle estilos)
            }
        }

    def create(self, validated_data):
        """ Crea y retorna nuevo usuario desde el serializador """
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

    def update(self, instance, validated_data): # Se le pasa la instancia y datos validados para poder hacer login dandole el hash a la contraseña
        """ Actualiza cuenta del usuario """
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        
        return super().update(instance, validated_data)

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """ Serializador de ProfileFeedItem """

    class Meta:
        model = models.ProfileFeedItemm # Para que trabaje con el modelo ProfileFeedItemm para recibir la informacion
        fields = ('id', 'user_profile', 'status_text', 'create_on')
        extra_kwargs = {'user_profile': {'read_only': True}}