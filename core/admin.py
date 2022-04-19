from django.contrib import admin
from .models import Cargo, Servico, Funcionario, Ferramentas1, Ferramentas2, Testemunhas


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servicos', 'icone', 'ativo', 'modificado')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')


@admin.register(Ferramentas1)
class Ferramentas1Admin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'icone', 'ativo', 'modificado')


@admin.register(Ferramentas2)
class Ferramentas2Admin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'icone', 'ativo', 'modificado')


@admin.register(Testemunhas)
class TestemunhasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'descricao', 'imagem', 'ativo', 'modificado')