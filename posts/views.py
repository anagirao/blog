from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView,CreateView, UpdateView, DeleteView, DetailView
from posts.models import Post
from posts.forms import PostCreateForm
from django.urls import reverse_lazy 
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/post.html'
    ordering = ['-created_at']

class PostCreateView(LoginRequiredMixin, CreateView): 
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/createpost.html'
    success_url = reverse_lazy('posts:pagina_post')  #ordem de postagem

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['autor', 'post','categoria']
    template_name = 'posts/update.html'
    success_url = reverse_lazy('posts:pagina_post')

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    context_object_name = 'post' 
    template_name = 'posts/delete.html' #leva para o html do template
    success_url = reverse_lazy('posts:pagina_post')

class PostDetailView(DetailView):
    model = Post 
    context_object_name = 'posts'
    template_name = 'posts/detailpost.html'   