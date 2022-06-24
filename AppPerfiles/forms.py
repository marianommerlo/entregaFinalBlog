from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email= forms.EmailField(required= True)
    first_name= forms.CharField(required= True, label= 'Nombre')
    last_name= forms.CharField(required= True, label= 'Apellido')
    descripcion= forms.CharField(required= False, label= 'Sobre ti')
    web= forms.URLField(required= False)
    password1= forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2= forms.CharField(label= 'Confirmar Contraseña', widget= forms.PasswordInput)

    class Meta:
        model= User
        fields= ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts= {k:"" for k in fields}


class UserEditForm(UserCreationForm):
    #especificamos los campos del formulario
    email= forms.EmailField(required= False, label= 'Modificar Email')
    first_name= forms.CharField(required= False, label= 'Modificar Nombre')
    last_name= forms.CharField(required= False, label= 'Modificar Apellido')
    descripcion= forms.CharField(label= 'Modificar Sobre ti')
    web= forms.URLField(label= 'Modificar Web')
    password1= forms.CharField(required= False, label= 'Modificar Contraseña', widget= forms.PasswordInput)
    password2= forms.CharField(required= False, label= 'Confirmar Contraseña', widget= forms.PasswordInput)

  
    class Meta:
        model= User
        fields= ['email', 'last_name', 'first_name', 'descripcion', 'web', 'password1', 'password2', ]
        help_texts= {k:"" for k in fields} #Para que no se vean las ayudas para crear contraseña
