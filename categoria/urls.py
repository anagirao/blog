from django.urls import path
from categoria.views import CategoriaListView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView

app_name = 'categoria'

urlpatterns = [
    path('categoria', CategoriaListView.as_view(),name='categorias_categoria'),
    path('adicionarcategoria', CategoriaCreateView.as_view(), name='adicionar_categoria'),
    path('categoria/<int:pk>/editar',CategoriaUpdateView.as_view(), name='updatecat_post'),
    path('categoria/<int:pk>/deletar',CategoriaDeleteView.as_view(), name='deletecat_categoria'),
]