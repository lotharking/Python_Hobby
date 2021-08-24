from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Recipe

from recipe.serializers import RecipeSerializer

RECIPE_URL = reverse('recipe:recipe-list')

def create_user(**params): # Para pasarle la cantidad de argumentos que se desee
    return get_user_model().objects.create_user(**params)

def Sample_recipe(user, **params): 
    """ Crear y retornar una receta """
    defaults = {
        'title': 'Sample recipe',
        'time_minutes': 10,
        'price': 5.00
    }
    defaults.update(params)
    return Recipe.objects.create(user=user, **defaults)

class PublicRecipeApiTest(TestCase):
    """ Test acceso no autenticado al api """
    def setUp(self):
        self.client = APIClient()
        self.user = create_user(
            email ='test@test.com',
            password ='testpass'
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_recipes(self):
        """ Probar obtener lista de recetas """
        Sample_recipe(user=self.user)
        Sample_recipe(user=self.user)

        res= self.client.get(RECIPE_URL)

        recipes = Recipe.objects.all().order_by('id')
        serializer = RecipeSerializer(recipes, many = True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_recipes_limited_to_user(self):
        """ Obtener la receta para un usuario """
        user2 = create_user(
            email ='otro@test.com',
            password = 'testpass'
        )
        Sample_recipe(user=user2)
        Sample_recipe(user=self.user)

        res=self.client.get(RECIPE_URL)

        recipes = Recipe.objects.filter(user=self.user)
        serializer = RecipeSerializer(recipes, many = True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data),1)
        self.assertEqual(res.data, serializer.data)



# class PrivateRecipeApiTest(TestCase):
#     """ Test acceso autenticado al api """
#     def setUp(self):
#         self.client = APIClient()