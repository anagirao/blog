from django.urls import path
from categorias.views import CategoriaListView, CategoriaCreateView

app_name = 'categoria'

urlpatterns = [
    path('categoria', CategoriaListView.as_view(),name='categorias_categoria'),
    path('adicionar', CategoriaCreateView.as_view(), name='addcat_categoria'),
]