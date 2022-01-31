from .models import Usuario


def has_perm(user, permission):

    try:

        return user.is_authenticated and user.usuario.estado == Usuario.HABILITADO and user.usuario.perfil.permisos.filter(codename=permission).exists()

    except Exception:

        return False
