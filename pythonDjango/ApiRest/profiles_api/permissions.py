from rest_framework import permissions

""" Creacion de clase permisos para dar permisos personalizados a usuaios """
class UpdateOwnProfile(permissions.BasePermission):
    """ Permite al usuario editar su propio perfil """

    def has_object_permission(self, request, view, obj):
        """ Chequear si el usuario esta editando su propio perfil """

        if request.method in permissions.SAFE_METHODS:
            return True

        """ Valida si el objeto a editar tiene match con el que se esta autenticado """
        return obj.id == request.user.id
        # return super().has_object_permission(request, view, obj)