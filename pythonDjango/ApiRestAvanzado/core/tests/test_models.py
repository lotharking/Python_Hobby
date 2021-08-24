from django.test import TestCase
from django.contrib.auth import get_user_model
from unittest.mock import patch # 

from core import models

def sample_user(email='test@dtest.com', password='testpass'):
    """ Creacion de usuario de ejemplo """
    return get_user_model().objects.create_user(email,password)

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

    def test_new_user__email_normalized(self):
        """ Verifica que el email fue normalizado """
        email = 'test@ANDRES.com'
        user = get_user_model().objects.create_user(email, 'Testpass123')

        self.assertEqual(user.email,email.lower()) # email.lower se encarga de normalizar y poner en minuscula

    def test_new_user_invalid_email(self):
        """ Cuando nuevo usuario da un email invalido """
        with self.assertRaises(ValueError):
            user = get_user_model().objects.create_user(None, 'Testpass123')

    def test_create_new_superuser(self):
        """ Probar super usuario creado """
        
        email = 'test@andres.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_superuser(
            email = email,
            password = password
        )

        self.assertTrue(user.is_superuser) # is_superuser se agrega con permissionsmix
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """ Probar representacion en cadena de texto del tag """
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Meat'
        )
        self.assertEqual(str(tag),tag.name)

    def test_ingredient_str(self):
        """ Probar representacion en cadena de texto del ingrediente """
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Banana'
        )
        self.assertEqual(str(ingredient),ingredient.name)

    def test_recipe_str(self):
        """ Probar representacion en cadena de texto de las recetas """
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title='Steak and mushroom sauce',
            time_minutes=5,
            price =5.00
        )
        self.assertEqual(str(recipe),recipe.title)

    @patch('uuid.uuid4')
    def test_file_name_uuid(self, mock_uuid):
        """ Probar que una imagen ha sido guardada en el lugar correcto """
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid
        file_path =models.recipe_image_file_path(None, 'myimage.jpg')

        exp_path = f'upload/recipe/{uuid}.jpg'
        self.assertEqual(file_path, exp_path)


