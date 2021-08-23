from django.forms.fields import EmailField
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status # Ayudan a poner los mensajes de error como se conocen con 200-400-500

CREATE_USER_URL = reverse('user:create')
TOKEN_URL = reverse('user:token')
ME_URL = reverse('user:me')

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
            'password': 'testpassword',
            'name': 'Test name'
        }
        create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """ Validar que la contraseña no es muy corta """
        payload = {
            'email': 'test@test.com',
            'password': 'pw',
            'name': 'Test name'
        }

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

        user_exist = get_user_model().objects.filter(
            email = payload['email']
        ).exists()

        self.assertFalse(user_exist)

    def test_create_token_for_user(self):
        """ Se prueba que el token se cree para el usuario """
        payload = {
            'email': 'test@test.com',
            'password': 'pw',
            'name': 'Test name'
        }
        create_user(**payload)
        res = self.client.post(TOKEN_URL, payload)

        self.assertIn('token', res.data) # Se valida que el token existe
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_token_invalid_credentials(self):
        """ Probar que el test no es creado con credenciales invalidas """

        create_user(email='user@test.com', password='testpass')
        payload = {
            'email': 'user@test.com',
            'password': 'wrong'
        }

        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', res.data) # Se valida si el token no existe
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_no_user(self):
        """ Probar que no se crea un token si no existe un usuarios """
        payload = {
            'email': 'test@test.com',
            'password': 'testpass'
        }
        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('token', res.data) # Se valida si el token no existe
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_missing_field(self):
        """ Probar que el email y contraseña sean requeridos """
        res = self.client.post(TOKEN_URL, {'email': 'one', 'password': ''})
        self.assertNotIn('token', res.data) # Se valida si el token no existe
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_url_user_unauthorized(self):
        """ Prueba que la autenticacion sea requerida para los usuarios """
        res = self.client.get(ME_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

class PrivateUserApiTest(TestCase):
    """ Testear el api para usuarios privados o autenticados """

    def setUp(self):
        """ Primera funcion para definir el APIClient"""
        self.user = create_user(
            email = 'test@test.com',
            password = 'testpassword',
            name='name'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user) # Autenticar al cliente

    def test_retrieve_profile_success(self):
        """ Probar obtener perfil para el usuario con login """
        res = self.client.get(ME_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, { # no se valida la contraseña por tema de seguridad
            'name': self.user.name,
            'email': self.user.email
        })
    
    def test_post_me_not_allowed(self):
        """ Prueba que el POST no sea permitido """
        res= self.client.post(ME_URL,{})
        self.assertEqual(res.status_code,status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_user_profile(self):
        """ Probar que el usuario esta siendo actualizado si esta autenticado """
        payload = {'name': 'new name','password': 'newpass1234'}

        res = self.client.patch(ME_URL,payload)
        self.user.refresh_from_db()
        self.assertEqual(self.user.name,payload['name'])
        self.assertTrue(self.user.check_password(payload['password']))
        self.assertEqual(res.status_code,status.HTTP_200_OK)