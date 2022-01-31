from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^usuarios/$', views.usuarios, name='usuarios'),
    url(r'^agregar-usuario/$', views.agregar_usuario, name='agregar_usuario'),
    url(r'^editar-usuario/(?P<id>[0-9]+)$', views.editar_usuario, name='editar_usuario'),
    url(r'^ajax/eliminar-usuario/$', views.ajax_eliminar_usuario, name='eliminar_usuario'),
]
