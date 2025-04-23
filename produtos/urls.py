from django.urls import path
from produtos import views

urlpatterns = [
    path('', views.visualizarLoja, name='loja'),
    path('<slug:categoria_slug>/', views.visualizarLoja, name='produtos_por_categoria'),
    
]