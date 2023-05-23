from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Agendamento, Barbeiro, Servicos, Horarios

def home(request):
    return render(request, "index.html")

def inicio(request):
    return redirect(home)

def about(request):
    return render(request, "about.html")

def login(request):
    return render(request, "register.html")

def register(request):
    if request.method == 'GET':
        return render(request, 'registration/register.html')
    else:
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse('já existe esse user cadastrado')
        else: 
            user = User.objects.create_user(first_name=name, username=username, password=password)
            user.save()
    return render(request, "registration/login.html")
        
        



@login_required
def agendar(request):
    varServicos = Servicos.objects.all()
    varHorarios = Horarios.objects.all()  
    return render(request, "agendar.html", {"servicos" : varServicos, "horarios" : varHorarios})

@login_required
def meusAgendamentos(request):
    varAgendamentos = Agendamento.objects.filter(user=request.user)
    varServicos = Servicos.objects.all()
    varHorarios = Horarios.objects.all()
    return render(request, "meusAgendamentos.html", {"agendamentos" : varAgendamentos, "servicos" : varServicos, "horarios" : varHorarios })

def salvar(request):
    varServico = request.POST.get("servico")
    varData = request.POST.get("data")
    varHorario = request.POST.get("horario")
    varUser = request.user
    Agendamento.objects.create(servico=varServico,data=varData, horario=varHorario, user=varUser)
    return redirect(meusAgendamentos)

def editar(request, id):
    varServicos = Servicos.objects.all()
    varHorarios = Horarios.objects.all()
    varAgendamentos = Agendamento.objects.get(id=id)
    return render(request, "editar.html", {"agendamentos" : varAgendamentos, "servicos" : varServicos, "horarios" : varHorarios})

def update(request, id):
    agendamento = Agendamento.objects.get(id=id)
    agendamento.servico = request.POST.get("servico")
    agendamento.data = request.POST.get("data")
    agendamento.horario = request.POST.get("horario")
    agendamento.save()
    return redirect(meusAgendamentos)

def delete(request, id):
    agendamento = Agendamento.objects.get(id=id)
    agendamento.delete()
    return redirect(meusAgendamentos)

@login_required
def barbeiro(request):
    varServicos = Servicos.objects.all()
    varHorarios = Horarios.objects.all()
    varAgendamentos = Agendamento.objects.all()
    return render(request, "barbeiro.html", {"servicos" : varServicos , "horarios" : varHorarios, "agendamentos" : varAgendamentos})    

def cadastrar_novo_servico(request):
    varNovo_Servico = request.POST.get("novo_servico")
    varValor = request.POST.get("valor")
    Servicos.objects.create(servicos=varNovo_Servico, valor=varValor)
    return redirect(barbeiro)

def deletar_servico(request, id):
    servico = Servicos.objects.get(id=id)
    servico.delete()
    return redirect(barbeiro)

def cadastrar_novo_horario(request):
    varNovo_Horario = request.POST.get("novo_horario")
    Horarios.objects.create(horarios=varNovo_Horario)
    return redirect(barbeiro)

def deletar_horario(request, id):
    horario = Horarios.objects.get(id=id)
    horario.delete()
    return redirect(barbeiro)