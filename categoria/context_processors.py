from categoria.models import Categoria

#--metodo utilizado para compartilhar objetos de forma globalizada no projeto

def menu_categoria(request):
    lista_categoria = Categoria.objects.all()
    return dict(opcoes = lista_categoria)   