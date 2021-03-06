import uuid
from django.db import models

from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1] # Extensão (png, jpeg, jpg)
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now_add=True)
    ativo = models.BooleanField('Ativo?', default=True)


    class Meta:
        abstract = True


class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    ) # Criação de opções de ícones
    servicos = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Ícone', max_length=12, choices=ICONE_CHOICES)


    class Meta:
        """Apresentação do método Servico"""
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    
    def __str__(self) -> str:
        return self.servicos


class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)


    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    
    def __str__(self) -> str:
        return self.cargo


class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')


    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    
    def __str__(self) -> str:
        return self.nome


class Ferramentas1(Base):
    """Armazena informação sobre os 3 cards da ESQUERDA"""

    titulo = models.CharField('Título', max_length=20)
    descricao = models.TextField('Descrição', max_length=100)
    
    ICON_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-layers', 'Design'),
        ('lni-leaf', 'Eco'),
    )
    icone = models.CharField('Ícone', max_length=20, choices=ICON_CHOICES)

    class Meta:
        verbose_name = 'Ferramenta1'
        verbose_name_plural = 'Ferramentas1'

    
    def __str__(self) -> str:
        return self.titulo


class Ferramentas2(Base):
    """Armazena informação sobre os 3 cards da Direita"""

    titulo = models.CharField('Título', max_length=20)
    descricao = models.TextField('Descrição', max_length=100)
    
    ICON_CHOICES = (
        ('lni-leaf', 'Eco'),
        ('lni-laptop-phone', 'Celular'),
        ('lni-rocket', 'Foguete'),
    )
    icone = models.CharField('Ícone', max_length=20, choices=ICON_CHOICES)

    class Meta:
        verbose_name = 'Ferramenta2'
        verbose_name_plural = 'Ferramentas2'

    
    def __str__(self) -> str:
        return self.titulo


class Testemunhas(Base):
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 75, 'height': 75, 'crop': True}})
    nome = models.CharField('Nome', max_length=20)
    cargo = models.CharField('Cargo', max_length=20)
    descricao = models.TextField('Descrição', max_length=100)


    class Meta:
        verbose_name = 'Testemunha'
        verbose_name_plural = 'Testemunhas'


    def __str__(self) -> str:
        return self.nome