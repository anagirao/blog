from django import forms
from comentarios.models import Comentarios

class ComentariosCreateForm(forms.ModelForm):
    class  Meta: #quando quer mudar a propriedade de alguém que foi herdado do que já exite no django
        model = Comentarios
        fields = ['post','comentario',] #outro aqui pra categoria
    