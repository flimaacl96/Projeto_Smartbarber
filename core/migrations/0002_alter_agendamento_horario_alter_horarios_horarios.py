# Generated by Django 4.1.2 on 2023-05-15 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='horario',
            field=models.CharField(max_length=12, verbose_name='horario'),
        ),
        migrations.AlterField(
            model_name='horarios',
            name='horarios',
            field=models.CharField(max_length=12, verbose_name='horarios'),
        ),
    ]
