from django import forms
from posts.models import Post

class PostCreateForm(forms.ModelForm):
    class  Meta: #quando quer mudar a propriedade de alguém que foi herdado do que já exite no django
        model = Post
        fields = ['autor', 'categoria', 'post','image'] #outro aqui pra categoria
    