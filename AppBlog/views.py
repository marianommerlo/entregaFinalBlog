from django.shortcuts import render, get_object_or_404
from AppBlog.models import *
from django.db.models import Q
from django.core.paginator import Paginator


def inicio(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True)

    if queryset:
        posts = Post.objects.filter(Q(titulo__icontains = queryset) | Q(subtitulo__icontains = queryset)).distinct()

    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    return render(request, 'AppBlog/inicio.html', {'posts': posts})


def detallePost(request, slug):
    post = get_object_or_404(Post, slug = slug)
    return render(request, 'AppBlog/post.html', {'detalle_post': post})
    

def finanzaspersonales(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Finanzas Personales'))
    
    if queryset:
        posts = Post.objects.filter(Q(titulo__icontains = queryset) | Q(subtitulo__icontains = queryset), estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Finanzas Personales')).distinct()
    
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'AppBlog/finanzaspersonales.html', {'posts': posts})

def inversiones(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Inversiones'))
    
    if queryset:
        posts = Post.objects.filter(Q(titulo__icontains = queryset) | Q(subtitulo__icontains = queryset), estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Inversiones')).distinct()
    
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'AppBlog/inversiones.html', {'posts': posts})

def seguros(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Seguros'))
    if queryset:
        posts = Post.objects.filter(Q(titulo__icontains = queryset) | Q(subtitulo__icontains = queryset), estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Seguros')).distinct()

    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'AppBlog/seguros.html', {'posts': posts})

def nofunciona(request):
    return render(request, 'AppBlog/noFunciona.html')
