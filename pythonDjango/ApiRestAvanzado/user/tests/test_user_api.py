from django.forms.fields import EmailField
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status # Ayudan a poner los mensajes de error como se conocen con 200-400-500

CREATE_USER_URL = reverse('user:create')

def create_user(**params): # Para pasarle la cantidad de argumentos que se desee
    return get_user_model().objects.create_user(**params)

class PublicUserApiTest(TestCase): # Test publicos(se separa el tipo de usuarios)
    """ Testear el api para usuarios publicos """
    def setUp(self):        
        """ Primera funcion para definir el APIClient"""
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """ Probar crear usuario con un payload exitoso """
        payload = {
            'email': 'test@test.com',
            'password': 'testpassword',
            'name': 'Test name'
        }

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        user = get_user_model().objects.get(**res.data) # Con esto obtenemos los datos del cliente -- **res.data

        self.assertTrue(user.check_password(payload['password']))

        self.assertNotIn('password', res.data) # Asegurarse que nos e pase la contraseña

    def test_user_exist(self):
        """ probar crear un usuario que ya existe y falla """
        payload = {
            'email': 'test@test.com',
            'password': 'testpassword'
        }
        create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """ Validar que la contraseña no es muy corta """
        payload = {
            'email': 'test@test.com',
            'password': 'pw'
        }

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

        user_exist = get_user_model().objects.filter(
            email = payload['email']
        ).exists()

        self.assertFalse(user_exist)

