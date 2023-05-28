from django.contrib import admin
from .models import Filme, Categoria, Cliente, Locacao

admin.site.register(Filme)
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Locacao)
