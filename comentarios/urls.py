from django.urls import path
from comentarios.views import ComentariosListView,ComentariosCreateView, ComentariosUpdateView, ComentariosDeleteView

app_name = 'comentarios'

urlpatterns = [
    path('comentarios', ComentariosListView.as_view(),name='comentario_comentarios'),
    path('criarcomentario', ComentariosCreateView.as_view(),name='criarcoment_comentarios'),
    path('comentarios/<int:pk>/editar',ComentariosUpdateView.as_view(), name='updatecoment_comentarios'),
    path('comentarios/<int:pk>/deletar',ComentariosDeleteView.as_view(), name='deletecoment_comentarios'),
    
]
