from django.contrib import admin
from django.urls import path
from gerenciador.views import index_html, lista_locacao, lista_filmes

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index_html, name="index"),
    path("lista_locacao",lista_locacao, name="lista_locacao" ),
    path("lista_filmes",lista_filmes, name="lista_filmes" ),
]
