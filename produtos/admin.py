from django.contrib import admin
from .models import Produto

# Register your models here.
class ProdutoAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug' : ('produto_nome' ,)
    }
    list_display = ('produto_nome','slug', 'imagens', 'categoria', )
    
admin.site.register(Produto, ProdutoAdmin) 