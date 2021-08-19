from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Tag

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
