from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, CreateView
from categoria.models import Categoria
from django.urls import reverse_lazy 
# Create your views here.

class CategoriaListView(Listview):
    model = Categoria
    context_object_name = 'categoria'
    template_name = 'categoria/categorias.html'
    success_url = reverse_lazy('posts:pagina_post')

class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaCreateForm
    template_name = 'categoria/categorias.html'