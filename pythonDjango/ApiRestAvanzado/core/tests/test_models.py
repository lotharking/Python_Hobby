from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):
    """ Va a probar que la funcion helper del modelo pueda crear un nuevo usuario """

    def test_create_user_email_successful(self):
        """ Prueba creando un nuevo usuario con un email correctamente """

        email = 'test@andres.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))