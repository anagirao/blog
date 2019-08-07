from django.shortcuts import render
from comentarios.models import Comentarios
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 
from comentarios.forms import ComentariosCreateForm
# Create your views here.

class ComentariosListView(ListView):
    model = Comentarios
    context_object_name = 'comentarios' #o que vai ser chamado no for do html
    template_name = 'comentario/listcomentario.html'
    ordering = ['-created_at']

class ComentariosCreateView(CreateView): 
    model = Comentarios
    form_class = ComentariosCreateForm
    template_name = 'comentario/createcomentario.html'
    success_url = reverse_lazy('comentarios:comentario_comentarios')    

class ComentariosUpdateView(UpdateView):
    model = Comentarios
    fields = ['comentario']
    template_name = 'comentario/updatecoment.html'
    success_url = reverse_lazy('comentarios:comentario_comentarios')  
    
class ComentariosDeleteView(DeleteView):
    model = Comentarios
    context_object_name = 'comentarios' 
    template_name = 'comentario/deletecoment.html' #leva para o html do template
    success_url = reverse_lazy('comentarios:comentario_comentarios')