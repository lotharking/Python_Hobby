from core import admin
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse # ayuda en lugar de escribir el url manualmente por si se llega a cambiar

class AdminSiteTests(TestCase):

    def setUp(self):
        """ Es la funcion que se corre en los test antes de hacer los test """
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email = 'admin@andres.com',
            password = 'password123'
        )

        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email = 'test@andres.com',
            password = 'pass123',
            name = 'Test user nombre completo'
        )

    def test_users_listed(self):
        """ Testear que los usuarios han sido enlistados en la pagina de usuario """
        url = reverse('admin:core_user_changelist') # genera el url para la lista de usuarios que tenemos
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """ Prueba que la pagina editada por el usuario funciona """
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)