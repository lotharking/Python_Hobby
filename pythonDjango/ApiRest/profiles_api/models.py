from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings
from django.db.models.base import Model # Obtener los settings que se definieron anteriormente

class UserProfileManager(BaseUserManager):
    """ Manager para perfiles de usuario, el cual permite especificar funciones
     para manipular lo que tenemos dentro de los objetos de user profile """

    def create_user(self, email, name, password=None):
        """ Crear nuevo UserProfile """
        if not email:
            raise ValueError('Usuario debe tener un email')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name) # crear modelo de usuario

        user.set_password(password) # Crearle contraseña al usuario
        user.save(using = self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True # Se especifica automaticamente cuando tenemos 'PermissionsMixin'
        user.is_staff = True
        user.save(using = self._db)

        return user

        

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """modelo base de datos para usuarios en el sistema"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True) # Valida si el usuario esta activo
    is_staff = models.BooleanField(default=False) # Valida si el usuario es miembro del equipo

    objects = UserProfileManager() # Objeto para que django sepa manejar los usuarios

    USERNAME_FIELD = 'email' # Autenticar con email y no con usuario
    REQUIRED_FIELDS = ['name'] 

    def get_full_name(self):
        '''Obtener nombre completo del usurio'''
        return self.name

    def get_short_name(self):
        '''Obtener nombre completo del usurio'''
        return self.name
    def __str__(self):
        '''cadena representando el usuario'''
        return self.email

class ProfileFeedItemm(models.Model):
    """ Perfil de estatus update, como su nombre lo indica, sera quien nos permita mantener los 
    recursos del usuario y traer o actualizar los que se requieran"""
    user_profile = models.ForeignKey( # Recordar que la ForeignKey permite hacer herencia entre objetos
        settings.AUTH_USER_MODEL, # Se usa de esta manera para poder actualizar el modelo de registro de usuario de Django en Settings.py
        on_delete=models.CASCADE # Si borramos el usuario se borran todos sus post y es necesario con el ForeignKey
    )

    status_text = models.CharField(max_length=255)
    create_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """ Retornar el texto como cadena """
        return self.status_text