"""EjemploA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import HomeView,AdministradoresView,EstudiantesView,CrearEstudiantesView,CrearEstudianteAutsView,CrearArticulosView,CrearComentariosView,CrearAdministradoresView,IniciosesionView,RegistroView,LoginView,ListarEstudiantesView,ListarEstudianteAutsView,ListarArticulosView,ListarComentariosView,ListarAdministradoresView,EditarEstudiantesView,EditarEstudianteAutsView,EditarArticulosView,EditarComentariosView,EditarAdministradoresView
from Apps.home import views

app_name='home'

urlpatterns = [
    path('',HomeView.as_view(), name='homeapp'),
    path('administradores/',AdministradoresView.as_view(), name='administradoresapp'),
    path('estudiantes/',EstudiantesView.as_view(), name='estudiantesapp'),
    path('crearestudiantes/',CrearEstudiantesView.as_view(), name='crearestudiantesapp'),
    path('crearestudianteauts/',CrearEstudianteAutsView.as_view(), name='crearestudianteautsapp'),
    path('creararticulos/',CrearArticulosView.as_view(), name='creararticulosapp'),
    path('crearcomentarios/',CrearComentariosView.as_view(), name='crearcomentariosapp'),
    path('crearadministradores/',CrearAdministradoresView.as_view(), name='crearadministradoresapp'),
    path('iniciosesion/',IniciosesionView.as_view(), name='iniciosesionapp'),
    path('registro/',RegistroView.as_view(), name='registroapp'),
    path('login/',LoginView.as_view(), name='loginapp'),
    path('listarestudiantes/',ListarEstudiantesView.as_view(), name='listarestudiantesapp'),
    path('listarestudianteauts/',ListarEstudianteAutsView.as_view(), name='listarestudianteautsapp'),
    path('listararticulos/',ListarArticulosView.as_view(), name='listararticulosapp'),
    path('listarcomentarios/',ListarComentariosView.as_view(), name='listarcomentariosapp'),
    path('listaradministradores/',ListarAdministradoresView.as_view(), name='listaradministradoresapp'),
    path('editarestudiantes/<int:pk>',EditarEstudiantesView.as_view(), name='editarestudiantesapp'),
    path('editarestudianteauts/<int:pk>',EditarEstudianteAutsView.as_view(), name='editarestudianteautsapp'),
    path('editararticulos/<int:pk>',EditarArticulosView.as_view(), name='editararticulosapp'),
    path('editarcomentarios/<int:pk>',EditarComentariosView.as_view(), name='editarcomentariosapp'),
    path('editaradministradores/<int:pk>',EditarAdministradoresView.as_view(), name='editaradministradoresapp'),

    
]
