from django.contrib import admin

from profiles_api import models

admin.site.register(models.UserProfile) # Acceso al admin para que pueda editar y crear modelos de user profile
admin.site.register(models.ProfileFeedItemm) # Acceso al admin para retroalimentacion de items

