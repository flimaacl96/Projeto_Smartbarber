from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),

    # URLS DE CADASTRO E LOGIN
    path('register/', views.register, name="register"),
    path('accounts/', include('django.contrib.auth.urls')),


    path('inicio', views.inicio, name="inicio"),
    path('about', views.about, name="about"),
    path('agendar/', views.agendar, name="agendar"),
    path('meusAgendamentos/', views.meusAgendamentos, name="meusAgendamentos"),
    path('clientesAgendados/', views.clientesAgendados, name="clientesAgendados"),
    path('salvar/', views.salvar, name="salvar"),
    path('editar/<int:id>', views.editar, name="editar"),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('barbeiro/', views.barbeiro, name="barbeiro"),
    path('cadastrar_novo_servico/', views.cadastrar_novo_servico, name="cadastrar_novo_servico"),
    path('deletar_servico/<int:id>', views.deletar_servico, name="deletar_servico"),
    path('cadastrar_novo_horario/', views.cadastrar_novo_horario, name="cadastrar_novo_horario"),
    path('deletar_horario/<int:id>', views.deletar_horario, name="deletar_horario")
]

