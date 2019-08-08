from django.shortcuts import render
from comentarios.models import Comentarios
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 
from comentarios.forms import ComentariosCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class ComentariosListView(ListView):
    model = Comentarios
    context_object_name = 'comentarios' #o que vai ser chamado no for do html
    template_name = 'comentario/listcomentario.html'
    ordering = ['-created_at']

class ComentariosCreateView(LoginRequiredMixin, CreateView): 
    model = Comentarios
    form_class = ComentariosCreateForm
    template_name = 'comentario/createcomentario.html'
    success_url = reverse_lazy('comentarios:comentario_comentarios')    

class ComentariosUpdateView(LoginRequiredMixin, UpdateView):
    model = Comentarios
    fields = ['comentario']
    template_name = 'comentario/updatecoment.html'
    success_url = reverse_lazy('comentarios:comentario_comentarios')  
    
class ComentariosDeleteView(LoginRequiredMixin, DeleteView):
    model = Comentarios
    context_object_name = 'comentarios' 
    template_name = 'comentario/deletecoment.html' #leva para o html do template
    success_url = reverse_lazy('comentarios:comentario_comentarios')