from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView,CreateView, UpdateView, DeleteView
from posts.models import Post
from posts.forms import PostCreateForm
from django.urls import reverse_lazy 

# Create your views here.

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/post.html'
    ordering = ['-created_at']

class PostCreateView(CreateView): 
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/createpost.html'
    success_url = reverse_lazy('posts:pagina_post')  #ordem de postagem

class PostUpdateView(UpdateView):
    model = Post
    fields = ['autor', 'post']
    template_name = 'posts/update.html'
    success_url = reverse_lazy('posts:pagina_post')

class PostDeleteView(DeleteView):
    model = Post
    context_object_name = 'post' 
    template_name = 'posts/delete.html' #leva para o html do template
    success_url = reverse_lazy('posts:pagina_post')