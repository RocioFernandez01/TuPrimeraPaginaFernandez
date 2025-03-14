
def index(request):
    posts = Post.objects.all()  
    return render(request, 'index.html', {'posts': posts})

# views.py
from django.shortcuts import render, redirect
from .forms import AutorForm, PostForm, ComentarioForm
from .models import Post, Autor, Comentario

# Vista para agregar un autor
def agregar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = AutorForm()
    return render(request, 'agregar_autor.html', {'form': form})

# Vista para agregar un post
def agregar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = PostForm()
    return render(request, 'agregar_post.html', {'form': form})


def agregar_comentario(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post  
            comentario.save()
            return redirect('detalle_post', post_id=post.id)  
    else:
        form = ComentarioForm()
    return render(request, 'agregar_comentario.html', {'form': form, 'post': post})

from django.shortcuts import render

def about(request):
    return render(request, 'about.html')

from django.shortcuts import render


def about(request):
    return render(request, 'about.html')

# blog/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post

def detalle_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'detalle_post.html', {'post': post})

from django.shortcuts import render
from .models import Post
from .forms import BusquedaForm

def buscar_post(request):
    form = BusquedaForm(request.GET)  
    resultados = []

    if form.is_valid():
        termino = form.cleaned_data.get('busqueda')
        if termino:
            resultados = Post.objects.filter(titulo__icontains=termino)  

    return render(request, 'buscar_post.html', {'form': form, 'resultados': resultados})

from django.shortcuts import render

def about(request):
    return render(request, 'about.html')

from django.shortcuts import render
from .models import Pagina

def lista_paginas(request):
    paginas = Pagina.objects.all()
    return render(request, 'blog/lista_paginas.html', {'paginas': paginas})

from django.urls import path
from . import views

urlpatterns = [
    path('paginas/', views.lista_paginas, name='lista_paginas'),
]

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('lista_paginas')  
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/registro.html', {'form': form})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def perfil(request):
    return render(request, 'usuarios/perfil.html')

from django.contrib.auth.forms import UserChangeForm

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'usuarios/editar_perfil.html', {'form': form})
