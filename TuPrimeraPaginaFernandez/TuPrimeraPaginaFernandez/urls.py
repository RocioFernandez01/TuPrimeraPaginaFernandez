"""
URL configuration for TuPrimeraPaginaFernandez project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from blog import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  
    path('post/<int:post_id>/', views.detalle_post, name='detalle_post'),  
    path('agregar_post/', views.agregar_post, name='agregar_post'),  
]

from django.urls import path
from . import views

urlpatterns = [
    path('agregar-autor/', views.agregar_autor, name='agregar_autor'),
    path('agregar-post/', views.agregar_post, name='agregar_post'),
    path('agregar-comentario/<int:post_id>/', views.agregar_comentario, name='agregar_comentario'),
]

from blog import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),  
]

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('paginas/', views.lista_paginas, name='lista_paginas'),
]

urlpatterns += [
    path('perfil/', views.perfil, name='perfil'),
]

urlpatterns += [
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
]
