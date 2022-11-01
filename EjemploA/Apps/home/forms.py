from django import forms
from .models import Estudiante, EstudianteAut, Articulo, Comentario, Administrador, Iniciosesion
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'

class EstudianteAutForm(forms.ModelForm):
    class Meta:
        model = EstudianteAut
        fields = '__all__'

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__'

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'

class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = '__all__'

class IniciosesionForm(forms.ModelForm):
    class Meta:
        model = Iniciosesion
        fields='__all__'

class RegistroForm(UserCreationForm):
    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields=(
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )