from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from .forms import EstudianteForm, EstudianteAutForm, ArticuloForm, ComentarioForm, AdministradorForm, IniciosesionForm, RegistroForm
from django.urls import reverse_lazy 
from .models import Usuario, Estudiante, EstudianteAut, Articulo, Comentario, Administrador
from django.contrib.auth.views import LoginView

# Create your views here.

class HomeView(TemplateView):
    template_name='home.html'

class AdministradoresView(TemplateView):
    template_name='administradores.html'

class EstudiantesView(TemplateView):
    template_name='estudiantes.html'

class CrearEstudiantesView(CreateView):
    template_name='crearestudiantes.html'
    form_class = EstudianteForm
    success_url = reverse_lazy('home:listarestudiantesapp')

class EditarEstudiantesView(UpdateView):
    template_name='editarestudiantes.html'
    model = Estudiante
    form_class = EstudianteForm
    success_url = reverse_lazy('home:listarestudiantesapp')

class CrearEstudianteAutsView(CreateView):
    template_name='crearestudianteauts.html'
    form_class = EstudianteAutForm
    success_url = reverse_lazy('home:listarestudianteautsapp')

class EditarEstudianteAutsView(UpdateView):
    template_name='editarestudianteauts.html'
    model = EstudianteAut
    form_class = EstudianteAutForm
    success_url = reverse_lazy('home:listarestudianteautsapp')

class CrearArticulosView(CreateView):
    template_name='creararticulos.html'
    form_class = ArticuloForm
    success_url = reverse_lazy('home:listararticulosapp')

class EditarArticulosView(UpdateView):
    template_name='editararticulos.html'
    model = Articulo
    form_class = ArticuloForm
    success_url = reverse_lazy('home:listararticulosapp')

class CrearComentariosView(CreateView):
    template_name='crearcomentarios.html'
    form_class = ComentarioForm
    success_url = reverse_lazy('home:listarcomentariosapp')

class EditarComentariosView(UpdateView):
    template_name='editarcomentarios.html'
    model = Comentario
    form_class = ComentarioForm
    success_url = reverse_lazy('home:listarcomentariosapp')

class CrearAdministradoresView(CreateView):
    template_name='crearadministradores.html'
    form_class = AdministradorForm
    success_url = reverse_lazy('home:listaradministradoresapp')

class EditarAdministradoresView(UpdateView):
    template_name='editaradministradores.html'
    model = Administrador
    form_class = AdministradorForm
    success_url = reverse_lazy('home:listaradministradoresapp')

class IniciosesionView(TemplateView):
    template_name='iniciosesion.html'

class CrearIniciosesionView(CreateView):
    template_name ='iniciosesion.html'
    form_class = IniciosesionForm
    success_url=reverse_lazy('home:homeapp')

class RegistroView(CreateView):
    model = Usuario
    form_class = RegistroForm
    success_url=reverse_lazy('home:homeapp')

class LoginView(LoginView):
    template_name ='iniciosesion.html'

class ListarEstudiantesView(ListView):
    template_name='listarestudiantes.html'
    model = Estudiante

    def get_queryset(self):
        vNombre = self.request.GET.get('nombre')
        if(vNombre):
            return Estudiante.objects.filter(nombre__icontains=vNombre)
        else:
            return Estudiante.objects.all()

class ListarEstudianteAutsView(ListView):
    template_name='listarestudiantesauts.html'
    model = EstudianteAut
    
    def get_queryset(self):
        vNombre = self.request.GET.get('nombre')
        if(vNombre):
            return EstudianteAut.objects.filter(nombre__icontains=vNombre)
        else:
            return EstudianteAut.objects.all()

class ListarArticulosView(ListView):
    template_name='listararticulos.html'
    model = Articulo

    def get_queryset(self):
        vNombre = self.request.GET.get('nombre')
        if(vNombre):
            return Articulo.objects.filter(nombre__icontains=vNombre)
        else:
            return Articulo.objects.all()

class ListarComentariosView(ListView):
    template_name='listarcomentarios.html'
    model = Comentario

    def get_queryset(self):
        vNombre = self.request.GET.get('comentario')
        if(vNombre):
            return Comentario.objects.filter(comentario__icontains=vNombre)
        else:
            return Comentario.objects.all()

class ListarAdministradoresView(ListView):
    template_name='listaradministradores.html'
    model = Administrador

    def get_queryset(self):
        vNombre = self.request.GET.get('nombre')
        if(vNombre):
            return Administrador.objects.filter(nombre__icontains=vNombre)
        else:
            return Administrador.objects.all()