# Generated by Django 5.0.6 on 2024-06-19 14:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materias', '0001_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='docente',
            field=models.ManyToManyField(related_name='docente_materia', to='usuarios.teacher'),
        ),
        migrations.AddField(
            model_name='materia',
            name='estudiante',
            field=models.ManyToManyField(related_name='inscripcion', to='usuarios.student'),
        ),
        migrations.AddField(
            model_name='tarea',
            name='materia',
            field=models.ManyToManyField(related_name='tarea_materia', to='materias.materia'),
        ),
        migrations.AddField(
            model_name='entrega',
            name='tarea',
            field=models.ManyToManyField(related_name='tarea_entrega', to='materias.tarea'),
        ),
        migrations.AddField(
            model_name='entrega',
            name='tipo_archivo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='materias.tipoarchivo'),
        ),
    ]
