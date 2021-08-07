""" Se usa para convertir informacion json, a traves de el se agrega el input, post, update, etc. 
Para poder recibir el contenido que se esta posteando al api """

from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """ Serializa un campo para probar nuestro APIView """
    name = serializers.CharField(max_length=10)