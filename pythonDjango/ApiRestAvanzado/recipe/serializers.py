from rest_framework import serializers

from core.models import Ingredient, Recipe, Tag

class TagSerializer(serializers.ModelSerializer):
    """ Serializador para objeto de Tag """
    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_Fields = ('id',)

class IngredientSerializer(serializers.ModelSerializer):
    """ Serializador para objeto de Ingredientes """
    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_Fields = ('id',)

class RecipeSerializer(serializers.ModelSerializer):
    """ Serializador para objeto de Recetas """
    class Meta:
        model = Recipe
        fields = ('id', 'title')
        read_only_Fields = ('id',)