from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from categoria.models import Categoria
from produtos.models import Produto

def visualizarLoja(request, categoria_slug=None):
    categorias = None
    produtos = None

    if categoria_slug != None:
        categorias = get_object_or_404(Categoria, slug=categoria_slug)
        produtos = Produto.objects.all().filter(categoria = categorias, esta_disponivel = True)
        produtos_quant = produtos.count()
    
    else:
        produtos = Produto.objects.all().filter(esta_disponivel = True)
        produtos_quant = produtos.count()

        context ={
            'produtos' : produtos,
            'produtos_quant' : produtos_quant
        }
    return render(request, 'loja/loja.html', context)
