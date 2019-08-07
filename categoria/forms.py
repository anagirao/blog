from django import forms
from categoria.models import Categoria

class CategoriaCreateForm(forms.ModelForm):
    class  Meta: #quando quer mudar a propriedade de alguém que foi herdado do que já exite no django
        model = Categoria
        fields = ['categoria', 'post',] #outro aqui pra categoria