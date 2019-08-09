from django.urls import path
from posts.views import PostListView, PostCreateView, PostUpdateView, PostDeleteView, PostDetailView

app_name = 'posts'

urlpatterns = [
    path('post', PostListView.as_view(),name='pagina_post'),
    path('adicionar', PostCreateView.as_view(), name='criar_post'),
    path('posts/<int:pk>/editar',PostUpdateView.as_view(), name='update_post'),
    path('posts/<int:pk>/deletar',PostDeleteView.as_view(), name='delete_post'),
    path('posts/<int:pk>/detalhes', PostDetailView.as_view(),name='detail_post'),
]
