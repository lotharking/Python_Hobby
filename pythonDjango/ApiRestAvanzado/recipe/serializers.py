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
    ingredients =serializers.PrimaryKeyRelatedField( # Se emplea de esta manera debido a que se maneja un manytomany en el modelo
        many=True, # Es un campo many
        queryset = Ingredient.objects.all()
    )

    tags =serializers.PrimaryKeyRelatedField( # Se emplea de esta manera debido a que se maneja un manytomany en el modelo
        many=True, # Es un campo many
        queryset = Tag.objects.all()
    )

    class Meta:
        model = Recipe
        fields = ('id', 'title', 'ingredients', 'tags', 'time_minutes', 'price', 'link')
        read_only_Fields = ('id',)

class RecipeDetailSerializer(RecipeSerializer):
    """ Serializador para ver detalles de una receta """
    ingredients =IngredientSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
