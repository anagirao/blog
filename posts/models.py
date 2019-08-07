from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#lembrando que qualquer alteração aqui, deve ser feito makemigrations
class Post(models.Model):
    autor = models.ForeignKey("users.User", verbose_name='autor', on_delete=models.CASCADE)
    categoria = models.ForeignKey("categoria.Categoria", verbose_name='categoria', on_delete=models.CASCADE)
    post = models.TextField(verbose_name='texto') 
    created_at = models.DateTimeField( auto_now=True, verbose_name='criado em')

    def __str__(self):
        return f'post {self.pk} | Publicado por {self.autor} | em {self.created_at}'