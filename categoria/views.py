from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from categoria.models import Categoria
from django.urls import reverse_lazy 
from categoria.forms import CategoriaCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class CategoriaListView(ListView):
    model = Categoria
    context_object_name = 'categoria'
    success_url = reverse_lazy('posts:pagina_post')

class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = CategoriaCreateForm
    template_name = 'categoria/adicionar.html'
    success_url = reverse_lazy('posts:pagina_post')

class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Categoria
    fields = ['Categoria']
    template_name = 'categoria/updatecat.html'
    success_url = reverse_lazy('posts:pagina_post')

class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    context_object_name = 'categoria' 
    template_name = 'categoria/deletecat.html' #leva para o html do template
    success_url = reverse_lazy('posts:pagina_post')    
    