from django.urls import re_path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from QP_Shift import views, settings
from django.contrib import admin
from django.contrib.auth.views import LoginView
from shifts import views as shiftviews

urlpatterns = [

    re_path(r'^$', shiftviews.records, name='records'),
    re_path(r'^', include('shifts.urls')),
    re_path(r'^api/', include('api.urls')),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^login/', LoginView.as_view(), name='login'),
    re_path(r'^informacion-personal/', views.informacion_personal, name='informacion_personal'),
    re_path(r'^cerrar-sesion/$', views.cerrar_sesion, name='cerrar_sesion')
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
