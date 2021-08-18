from django.contrib.auth import get_user_model
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