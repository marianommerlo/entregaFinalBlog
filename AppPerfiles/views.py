from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def bienvenido(request):
    if request.user.is_authenticated:
        #avatar= Avatar.objects.filter(user= request.user)
        return render(request, 'AppPerfiles/bienvenido.html')# {'url': avatar[0].avatar.url})
    else:
        return render(request, template_name='AppPerfiles/bienvenido.html')


def login_request(request):

    if request.method == "POST":
        formulario= AuthenticationForm(request, data= request.POST)

        if formulario.is_valid():
            usuario= formulario.cleaned_data.get('username')
            clave= formulario.cleaned_data.get('password')

            user= authenticate(username= usuario, password= clave)
            
            if user is not None:
                login(request, user)
                return render(request, 'AppPerfiles/bienvenido.html', {'mensaje': f'Bienvenido al Sistema'})

            else:
                return render(request, 'AppPerfiles/login.html', {'formulario': formulario, 'mensaje': 'Usuario o clave incorrecto, vuelva a loguearse'})
        
        else:
            return render(request, 'AppPerfiles/login.html', {'formulario': formulario, 'mensaje': 'Formulario inválido, vuelva a loguearse'})
    
    else:
        formulario= AuthenticationForm()
        return render(request, 'AppPerfiles/login.html', {'formulario': formulario})


def registro(request):
    if request.method == 'POST':
        formulario = UserRegistrationForm(request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data.get('username')
            formulario.save()

            return render(request, 'AppPerfiles/bienvenido.html', {'mensaje': f'Usuario {username} creado satisfactoriamente'})

        else:
            return render(request, 'AppPerfiles/bienvenido.html', {'mensaje': 'No se pudo crear el usuario, intente nuevamente'})

    else:
        formulario= UserRegistrationForm()
        return render(request, 'AppPerfiles/registro.html', {'formulario': formulario})


#EDICION DE PERFIL-------------------------------------------------------------------------------------------

def detallePerfil(request):
    perfiles = Perfil.objects.all()
    contexto = {'perfiles': perfiles}
    
    return render(request, 'AppPerfiles/detallePerfil.html', contexto)

def editarPerfil(request):
    usuario = request.user

    if request.method == 'POST':
        formulario = UserEditForm(request.POST, instance= usuario)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario.first_name = informacion.get('first_name')
            usuario.last_name = informacion.get('last_name')
            usuario.email = informacion.get('email')
            usuario.descripcion = informacion.get('descripcion')
            usuario.web = informacion.get('web')
            usuario.save()

            return render(request, 'AppPerfiles/bienvenido.html', {'usuario': usuario, 'mensaje': f'Se editó exitosamente el perfil de {usuario}'})

    else:
        formulario= UserEditForm(instance= usuario)
        
    return render(request, 'AppPerfiles/editarPerfil.html', {'formulario': formulario, 'usuario': usuario.username})


def eliminarPerfil(request, nombre):
    usuario = Perfil.objects.get(nombre = nombre)
    usuario.delete()
    
    usuarios = Perfil.objects.all()
    contexto = {'usuarios': usuarios}

    return render(request, 'AppBlog/inicio.html', contexto, {'mensaje': f'El perfil {usuario} fue eliminado'})