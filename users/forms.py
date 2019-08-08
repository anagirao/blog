from django import forms
from users.models import User
from django.contrib.auth.forms import UserCreationForm

class UserSignUpCreateForm(UserCreationForm):
    class  Meta: #quando quer mudar a propriedade de alguém que foi herdado do que já exite no django
        model = User
        fields = ['username', 'email'] #outro aqui pra categoria