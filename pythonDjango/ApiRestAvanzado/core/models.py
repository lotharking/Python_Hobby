from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
""" Indicaciones de importacion :
    AbstractBaseUser -> creamos un usario
    BaseUserManager -> creamos el manager de ese usuario creado
    PermissionsMixin -> dandole permisos al usuario
    """

class UserManager(BaseUserManager):
    """ Clase que indicara el manejo que se le da al usuario """
    def create_user(self, email, password=None,**extra_fields):
        """ Crea y guarda un nuevo usuario:
        extra_fields -> si se le pasa algun otro campo este argumento lo recibe """

        if not email:
            raise ValueError('Users must have an email')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password) # guardar la contraseña con un hasch
        user.save(using=self._db) # guarda el usuario
        
        return user

    def create_superuser(self, email, password):
        """ Crear super usuario """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """ Modelo personalizado de usuario que soporta hacer loggin con email en lugar del usuario """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'