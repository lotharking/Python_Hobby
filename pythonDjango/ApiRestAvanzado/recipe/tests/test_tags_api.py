from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Tag, Recipe

from recipe.serializers import TagSerializer

TAG_URL = reverse('recipe:tag-list')

def create_user(**params): # Para pasarle la cantidad de argumentos que se desee
    return get_user_model().objects.create_user(**params)

class PublicTagsApiTests(TestCase):
    """ Probar los api tags disponibles publicamente """

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """ Probar que el login sea requerido para obtener los tags """
        res= self.client.get(TAG_URL)
        self.assertEqual(res.status_code,status.HTTP_401_UNAUTHORIZED)

class PrivateTagsApiTests(TestCase):
    """ Probar los api tags disponibles privadamente """

    def setUp(self):
        self.user = create_user(
            email = 'test@test.com',
            password = 'testpassword'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user) # Autenticar al cliente

    def test_retrieve_tags(self):
        """ Probar obtener tags """
        Tag.objects.create(user=self.user,name='Meat')
        Tag.objects.create(user=self.user,name='Banana')

        res = self.client.get(TAG_URL)

        tags = Tag.objects.all().order_by('-name')
        serializer = TagSerializer(tags, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_tags_limited_to_user(self):
        """ Probar que los tags retornados sean del usuario """
        user2 = create_user(
            email = 'otro@test.com',
            password = 'testpass'
        )
        Tag.objects.create(user=user2,name='Raspberry')
        tag = Tag.objects.create(user=self.user, name= 'Comfort foot')

        res = self.client.get(TAG_URL)

        self.assertEqual(res.status_code,status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], tag.name)
        
    def test_create_tag_successful(self):
        """ Prueba creando nuevo tag """
        payload = {'name': 'Simple'}
        self.client.post(TAG_URL, payload)

        exists = Tag.objects.filter(
            user = self.user,
            name = payload['name']
        ).exists()

        self.assertTrue(exists)

    def test_create_tag_invalid(self):
        """ Prueba crear un nuevo tag con un payload invalido """
        payload = {'name': ''}
        res = self.client.post(TAG_URL, payload)

        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)

    def test_retrieve_tags_assigned_to_recipe(self):
        """ Prueba filtrando tags basado en la receta """
        tags1 = Tag.objects.create(user=self.user, name = 'Breakfast')
        tags2 = Tag.objects.create(user=self.user, name = 'Lunch')
        recipe = Recipe.objects.create(
            title='Coriander eggs on toast',
            time_minutes=10,
            price=5.00,
            user=self.user
        )
        recipe.tags.add(tags1)

        res= self.client.get(TAG_URL, {'assigned_only':1})

        serializer1 = TagSerializer(tags1)
        serializer2 = TagSerializer(tags2)

        self.assertIn(serializer1.data, res.data)
        self.assertNotIn(serializer2.data, res.data)

    def test_retrieve_tags_assigned_unique(self):
        """ Prueba filtro tags asignados por id unico """
        tags = Tag.objects.create(user=self.user, name = 'Breakfast')
        recipe1 = Recipe.objects.create(
            title='Pancakes',
            time_minutes=5,
            price=5.00,
            user=self.user
        )
        recipe1.tags.add(tags)
        recipe2 = Recipe.objects.create(
            title='Porridge',
            time_minutes=3,
            price=2.00,
            user=self.user
        )
        recipe2.tags.add(tags)
        
        res= self.client.get(TAG_URL, {'assigned_only':1})

        self.assertEqual(len(res.data), 1)