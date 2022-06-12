from django.contrib import admin
from AppBlog.models import *

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'fecha_creacion')

class AutorAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'apellido', 'email']
    list_display = ('apellido', 'nombre', 'email', 'fecha_creacion')

class PostsAdmin(admin.ModelAdmin):
    search_fields = ['titulo', 'autor__nombre', 'autor__apellido', 'categoria__nombre']
    list_display = ('titulo', 'autor', 'categoria', 'fecha_creacion')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post, PostsAdmin)

