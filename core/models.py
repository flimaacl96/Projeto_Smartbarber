from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth import get_user_model

    
class Agendamento(models.Model):
    id = models.AutoField(primary_key=True)
    servico = models.CharField(max_length=100, verbose_name='servico')
    valor = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


    def __str__(self):
        return self.servico 
    
    data = models.DateField(null=False, blank=False,verbose_name='data')
    horario = models.CharField(max_length=12, verbose_name='horario')

    



class Barbeiro(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, verbose_name='nome_barbeiro')

class Servicos(models.Model):
    id = models.AutoField(primary_key=True)
    servicos = models.CharField(max_length=100, verbose_name='servicos')
    valor = models.DecimalField(max_digits=6, decimal_places=2, default=0)

class Horarios(models.Model):
    id = models.AutoField(primary_key=True)
    horarios = models.CharField(max_length=12, verbose_name='horarios')

    def __str__(self):
        return self.horario.strftime('%m-%d-%YT%H:%m')




    
            

