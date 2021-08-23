from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Ingredient

from recipe.serializers import IngredientSerializer

INGREDIENT_URL = reverse('recipe:ingredient-list')

def create_user(**params): # Para pasarle la cantidad de argumentos que se desee
    return get_user_model().objects.create_user(**params)

class PublicIngredientsApiTest(TestCase):
    """ Probar api ingredientes accesibles publicamente """

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """ Probar que el login es requerido para acceder al endpoint"""
        res = self.client.get(INGREDIENT_URL)
        self.assertEqual(res.status_code,status.HTTP_401_UNAUTHORIZED)
        
class PrivateIngredientsApiTests(TestCase):
    """ Probar los api ingredients disponibles privadamente """
    
    def setUp(self):
        self.user = create_user(
            email = 'test@test.com',
            password = 'testpassword'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user) # Autenticar al cliente
        
    def test_retrieve_ingredient_list(self):
        """ Probar obtener lista de ingredientes """
        Ingredient.objects.create(user=self.user,name='kale')
        Ingredient.objects.create(user=self.user,name='salt')

        res = self.client.get(INGREDIENT_URL)

        ingredients = Ingredient.objects.all().order_by('-name')
        serializer = IngredientSerializer(ingredients, many = True)

        self.assertEqual(res.status_code,status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
        
    def test_ingredients_limited_to_user(self):
        """ Probar que los ingredientes retornados son los autenticados por el usuario """
        user2 = create_user(
            email = 'otro@test.com',
            password = 'testpass'
        )

        Ingredient.objects.create(user=user2,name='vinegar')
        ingredient = Ingredient.objects.create(user=self.user, name='tumeric')

        res = self.client.get(INGREDIENT_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data),1)
        self.assertEqual(res.data[0]['name'], ingredient.name)
        
    def test_create_ingredient_successful(self):
        """ Prueba creando nuevo ingrediente """
        payload = {'name': 'Chocolate'}

        self.client.post(INGREDIENT_URL,payload)

        exists = Ingredient.objects.filter(
            user=self.user,
            name=payload['name']
        ).exists()

        self.assertTrue(exists)

    def test_create_ingrediente_invalid(self):
        """ Prueba crear un nuevo ingrediente con un payload invalido """
        payload = {'name': ''}

        res = self.client.post(INGREDIENT_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)