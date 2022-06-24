from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .models import *
from ckeditor.fields import RichTextField
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostEditForm(forms.Form):
    #especificamos los campos del formulario
    titulo = forms.CharField(max_length = 90)	
    subtitulo = forms.CharField(max_length = 110)
    cuerpo = RichTextField(False)
    imagen = forms.URLField(max_length = 1100)
    categoria = forms.ModelChoiceField(queryset = Categoria.objects.all())

    class Meta:
        model = Post
        fields= ['titulo', 'subtitulo', 'cuerpo', 'imagen', 'categoria']
