from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_request, name= 'login'),
    path('logout/', LogoutView.as_view(template_name="AppRegistro/logout.html"), name= 'logout'),
    path('bienvenido/', bienvenido, name= 'bienvenido'),
    path('registro/', registro, name= 'registro'),
    path('perfil/list/', PerfilList.as_view(), name= 'perfil_listar'),
    path('perfil/detalle/<pk>/', PerfilDetalle.as_view(), name= 'perfil_detalle'),
    path('perfil/borrar/<pk>/', PerfilEliminacion.as_view(), name= 'perfil_borrar'),
    path('editarPerfil/', editarPerfil, name= 'editarPerfil'),
    
]   