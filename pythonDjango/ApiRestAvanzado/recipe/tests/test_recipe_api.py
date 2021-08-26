from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Recipe, Tag, Ingredient

from recipe.serializers import RecipeSerializer, RecipeDetailSerializer

import tempfile
import os

from PIL import Image


RECIPE_URL = reverse('recipe:recipe-list')

def image_upload_url(recipe_id):
    """ URL de retorno para imagen subida """
    return reverse('recipe:recipe-upload-image', args=[recipe_id])

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

def Sample_tag(user, name='Main course'): 
    """ Crear tag ejemplo """
    return Tag.objects.create(user=user, name=name)

def Sample_ingredient(user, name='Cinnamon'): 
    """ Crear ingrediente ejemplo """
    return Ingredient.objects.create(user=user, name=name)

def detail_url(recipe_id):
    """ Retorna receta detail url"""
    return reverse('recipe:recipe-detail', args=[recipe_id])

class PublicRecipeApiTest(TestCase):
    """ Test acceso no autenticado al api """
    def setUp(self):
        self.client = APIClient()

    def test_required_auth(self):
        """ Prueba autenticacion necesaria """
        res = self.client.get(RECIPE_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateRecipeApiTest(TestCase):
    """ Test acceso autenticado al api """
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

    def test_view_recipe_detail(self):
        """ Prueba ver los detalles de una receta """
        recipe= Sample_recipe(user=self.user)
        recipe.tags.add(Sample_tag(user=self.user))
        recipe.ingredients.add(Sample_ingredient(user=self.user))

        url = detail_url(recipe.id)
        res=self.client.get(url)

        serializer = RecipeDetailSerializer(recipe)
        self.assertEqual(res.data,serializer.data)

    def test_create_basic_recipe(self):
        """ Prueba para creacion de recetas """
        payload = {
        'title': 'Test recipe',
        'time_minutes': 30,
        'price': 10.00            
        }
        res = self.client.post(RECIPE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        recipe = Recipe.objects.get(id=res.data['id'])
        for key in payload.keys():
            self.assertEqual(payload[key], getattr(recipe, key))

    def test_create_recipe_with_tags(self):
        """ Prueba para creacion de recetas con tags """
        tag1 = Sample_tag(user=self.user, name='Tag 1')
        tag2 = Sample_tag(user=self.user, name='Tag 2')
        payload = {
        'title': 'Test recipe',
        'tags': {tag1.id, tag2.id},
        'time_minutes': 30,
        'price': 10.00            
        }
        res = self.client.post(RECIPE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        recipe = Recipe.objects.get(id=res.data['id'])
        tags = recipe.tags.all()
        self.assertEqual(tags.count(), 2)
        self.assertIn(tag1, tags)
        self.assertIn(tag2, tags)

    def test_create_recipe_with_ingredients(self):
        """ Prueba para creacion de recetas con ingredientes """
        ingredient1 = Sample_ingredient(user=self.user, name='Ingredient 1')
        ingredient2 = Sample_ingredient(user=self.user, name='Ingredient 2')
        payload = {
        'title': 'Test recipe',
        'ingredients': {ingredient1.id, ingredient2.id},
        'time_minutes': 45,
        'price': 15.00            
        }
        res = self.client.post(RECIPE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        recipe = Recipe.objects.get(id=res.data['id'])
        ingredients = recipe.ingredients.all()
        self.assertEqual(ingredients.count(), 2)
        self.assertIn(ingredient1, ingredients)
        self.assertIn(ingredient2, ingredients)


class RecipeImageUploadTest(TestCase):
    """ clase de pruebas para las imagenes """

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user('user', 'testpass')
        self.client.force_authenticate(self.user)
        self.recipe = Sample_recipe(user=self.user)

    def tearDown(self):
        self.recipe.image.delete()

    def test_upload_image_to_recipe(self):
        """ Prueba para subir imagen a la receta """
        url = image_upload_url(self.recipe.id)
        with tempfile.NamedTemporaryFile(suffix='.jpg') as ntf:
            img = Image.new('RGB', (10,10))
            img.save(ntf, format='JPEG')
            ntf.seek(0)
            res = self.client.post(url, {'image':ntf}, format = 'multipart')

        self.recipe.refresh_from_db()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn('image', res.data)
        self.assertTrue(os.path.exists(self.recipe.image.path))

    def test_upload_image_bad_request(self):
        """ Prueba subir imagen fallo """
        url = image_upload_url(self.recipe.id)
        res = self.client.post(url, {'image': 'notimage'}, format='multipart')

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_filter_recipes_by_tags(self):
        """ Prueba filtrar recetas por tags """
        recipe1 = Sample_recipe(user=self.user, title='Thai vegetable curry')
        recipe2 = Sample_recipe(user=self.user, title='Aubergine with tahini')
        tag1 = Sample_tag(user=self.user, name='Vegan')
        tag2 = Sample_tag(user=self.user, name='Vegetarian')
        recipe1.tags.add(tag1)
        recipe2.tags.add(tag2)
        recipe3 = Sample_recipe(user=self.user, title='Fish and chips')

        res = self.client.get(
            RECIPE_URL, 
            {'tags': '{},{}'.format(tag1.id, tag2.id)}
        )

        serializer1 = RecipeSerializer(recipe1)
        serializer2 = RecipeSerializer(recipe2)
        serializer3 = RecipeSerializer(recipe3)

        self.assertIn(serializer1.data, res.data)
        self.assertIn(serializer2.data, res.data)
        self.assertNotIn(serializer3.data, res.data)

    def test_filter_recipes_by_ingredients(self):
        """ Prueba filtrar recetas por ingredientes """
        recipe1 = Sample_recipe(user=self.user, title='Posh beans on toast')
        recipe2 = Sample_recipe(user=self.user, title='Chicken cacciatore')
        ingredient1 = Sample_ingredient(user=self.user, name='Feta cheese')
        ingredient2 = Sample_ingredient(user=self.user, name='Chicken')
        recipe1.ingredients.add(ingredient1)
        recipe2.ingredients.add(ingredient2)
        recipe3 = Sample_recipe(user=self.user, title='Steak and muchrooms')

        res = self.client.get(
            RECIPE_URL, 
            {'ingredients': '{},{}'.format(ingredient1.id, ingredient2.id)}
        )

        serializer1 = RecipeSerializer(recipe1)
        serializer2 = RecipeSerializer(recipe2)
        serializer3 = RecipeSerializer(recipe3)

        self.assertIn(serializer1.data, res.data)
        self.assertIn(serializer2.data, res.data)
        self.assertNotIn(serializer3.data, res.data)