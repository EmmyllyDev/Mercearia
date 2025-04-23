from django.shortcuts import render

from produtos.models import Produto

def visualizarHome(request):
    produtos = Produto.objects.all().filter(esta_disponivel = True)
    contexto = {
        'produtos' : produtos
    }

    return render(request, 'home.html', contexto)