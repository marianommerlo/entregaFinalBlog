from django.db import models
from ckeditor.fields import RichTextField

class Categoria(models.Model):
    nombre = models.CharField('Nombre de la Categoría', max_length = 100, null = False, blank = False)
    fecha_creacion = models.DateTimeField('Fecha de Creación', auto_now = False, auto_now_add = True)
    estado = models.BooleanField('Categoría Activa/No Activa', default = True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField('Nombre del Autor', max_length = 255, null = False, blank = False)
    apellido = models.CharField('Apellido del Autor', max_length = 255, null = False, blank = False)
    email = models.EmailField('Email', max_length = 255, null = False, blank = False)
    fecha_creacion = models.DateTimeField('Fecha de Creación', auto_now = False, auto_now_add = True)
    estado = models.BooleanField('Autor Activo/No Activo', default = True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.apellido + ', ' + self.nombre


class Post(models.Model):
    titulo = models.CharField('Título', max_length = 90, null = False, blank = False)
    slug = models.CharField('Slug', max_length = 100, null = False, blank = False)
    descripcion = models.CharField('Descripción', max_length = 110, null = False, blank = False)
    contenido = RichTextField('Contenido', blank = False, null = False)
    imagen = models.URLField(max_length = 1100, null = False, blank = False)
    #Atento acá porque se usa url si subo a heroku, no se puede almacenar imagenes.
    #En todo caso sera models.ImageField
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado', default = True)
    fecha_creacion = models.DateTimeField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo + ' por ' + self.autor.apellido + ', ' + self.autor.nombre
