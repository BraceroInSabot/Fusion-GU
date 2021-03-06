# Generated by Django 4.0.4 on 2022-04-19 20:18

import core.models
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testemunhas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now_add=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('imagem', stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Imagem')),
                ('nome', models.CharField(max_length=20, verbose_name='Nome')),
                ('cargo', models.CharField(max_length=20, verbose_name='Cargo')),
                ('descricao', models.TextField(max_length=100, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Testemunha',
                'verbose_name_plural': 'Testemunhas',
            },
        ),
    ]
