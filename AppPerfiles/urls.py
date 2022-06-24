from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_request, name= 'login'),
    path('logout/', LogoutView.as_view(template_name="AppPerfiles/logout.html"), name= 'logout'),
    path('bienvenido/', bienvenido, name= 'bienvenido'),
    path('registro/', registro, name= 'registro'),
    path('detallePerfil/', detallePerfil, name= 'detallePerfil'),
    path('editarPerfil/', editarPerfil, name= 'editarPerfil'),
    path('eliminarPerfil/<nombre>', eliminarPerfil, name= 'eliminarPerfil'),

]