from django.contrib import admin

from django.contrib import admin
from .models import Autor, Post, Comentario

admin.site.register(Autor)
admin.site.register(Post)
admin.site.register(Comentario)

