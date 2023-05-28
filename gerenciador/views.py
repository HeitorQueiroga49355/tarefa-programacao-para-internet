from django.shortcuts import render
from locadora.models import Locacao, Filme

def index_html(request):
    return render(request, 'index.html')

def lista_locacao(request):
    locacoes = Locacao.objects.all()
    return render(request, 'lista_locacao.html', {"locacoes": locacoes})

def lista_filmes(request):
    filmes = Filme.objects.all()
    return render(request, 'lista_filmes.html', {"filmes": filmes})

