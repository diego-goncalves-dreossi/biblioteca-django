from django.contrib import admin
from .models import Categoria, Livro, Emprestimo

# Register your models here.

admin.site.register(Livro)
admin.site.register(Categoria)
admin.site.register(Emprestimo)