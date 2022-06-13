from dataclasses import fields
from django.shortcuts import render
from .models import *
from django.contrib.auth.forms import AuthenticationForm #, UserCreationForm
from django.contrib.auth import login, authenticate #, logout
from AppRegistro.forms import UserRegistrationForm, UserEditForm #, AvatarForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User

#from http.client import HTTPResponse
#from django.http import HttpResponse


def bienvenido(request):
    if request.user.is_authenticated:
        #avatar= Avatar.objects.filter(user= request.user)
        return render(request, 'AppRegistro/bienvenido.html')# {'url': avatar[0].avatar.url})
    else:
        return render(request, template_name='AppRegistro/bienvenido.html')


def login_request(request):

    if request.method == "POST":
        formulario= AuthenticationForm(request, data= request.POST)

        if formulario.is_valid():
            usuario= formulario.cleaned_data.get('username')
            clave= formulario.cleaned_data.get('password')

            user= authenticate(username= usuario, password= clave)
            
            if user is not None:
                login(request, user)
                return render(request, 'AppRegistro/bienvenido.html', {'mensaje': f'Bienvenido al Sistema'})

            else:
                return render(request, 'AppRegistro/login.html', {'formulario': formulario, 'mensaje': 'Usuario o clave incorrecto, vuelva a loguearse'})
        
        else:
            return render(request, 'AppRegistro/login.html', {'formulario': formulario, 'mensaje': 'Formulario inválido, vuelva a loguearse'})
    
    else:
        formulario= AuthenticationForm()
        return render(request, 'AppRegistro/login.html', {'formulario': formulario})


def registro(request):
    if request.method == 'POST':
        formulario = UserRegistrationForm(request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data.get('username')
            formulario.save()

            return render(request, 'AppRegistro/bienvenido.html', {'mensaje': f'Usuario {username} creado satisfactoriamente'})

        else:
            return render(request, 'AppRegistro/bienvenido.html', {'mensaje': 'No se pudo crear el usuario, intente nuevamente'})

    else:
        formulario= UserRegistrationForm()
        return render(request, 'AppRegistro/registro.html', {'formulario': formulario})



#PERFIL-------------------------------------------------------------------------------------------

class PerfilList(LoginRequiredMixin, ListView):
    model = Perfil
    template_name = 'AppRegistro/perfil_listar.html'


class PerfilDetalle(LoginRequiredMixin, DetailView):
    model= Perfil
    template_name= 'AppRegistro/perfil_detalle.html'

class PerfilEdicion(UpdateView):
    model= Perfil
    success_url= reverse_lazy('perfil_listar')
    fields= ['nombre', 'apellido', 'email', 'web', 'descripcion', 'avatar']

class PerfilEliminacion(DeleteView):
    model= Perfil
    success_url= reverse_lazy('perfil_listar')
    fields= ['user', 'nombre', 'apellido', 'email']

@login_required
def editarPerfil(request):
    usuario= request.user

    if request.method == 'POST':
        formulario= UserEditForm(request.POST, instance= usuario)

        if formulario.is_valid():
            informacion= formulario.cleaned_data
            usuario.email= informacion['email']
            usuario.password1= informacion['password1']
            usuario.password2= informacion['password2']
            usuario.save()

            return render(request, 'AppRegistro/perfil_detalle.html', {'usuario': usuario, 'mensaje': f'Perfil de {usuario} editado satisfactoriamente'})

    else:
        formulario= UserEditForm(instance= usuario)
        
    return render(request, 'AppRegistro/editarPerfil.html', {'formulario': formulario, 'usuario': usuario.username})