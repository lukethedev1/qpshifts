from django.urls import re_path
from . import views

urlpatterns = [

    re_path(r'^records/$', views.records, name='records'),
    re_path(r'^cerrar-registros/$', views.cerrar_registro, name='cerrar_registro'),
    re_path(r'^exportar-registros-excel/$', views.exportar_registros_excel, name='exportar_registros_excel'),
    re_path(r'^exportar-detalle-registros-excel/$', views.exportar_detalle_registros_excel, name='exportar_detalle_registros_excel'),
    re_path(r'^exportar-registros-pdf/$', views.exportar_registros_pdf, name='exportar_registros_pdf'),
    re_path(r'^exportar-detalle-registros-pdf/$', views.exportar_detalle_registros_pdf, name='exportar_detalle_registros_pdf'),
    re_path(r'^records-detail/$', views.records_detail, name='records_detail')
]