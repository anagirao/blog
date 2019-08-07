from django.db import models

# Create your models here.
class Comentarios(models.Model):
    post = models.ForeignKey("posts.Post", verbose_name='post', on_delete=models.CASCADE)
    comentario = models.TextField(verbose_name='comentario')
    created_at = models.DateTimeField( auto_now=True)
    class Meta:
        verbose_name='Comentario'
        verbose_name_plural = 'Comentarios'