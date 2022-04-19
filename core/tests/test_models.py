import uuid
from django.test import TestCase
from model_mommy import mommy

from core.models import Ferramentas1, get_file_path


class GetFilePathTestCase(TestCase):

    def setUp(self):
        self.filename = f"{uuid.uuid4()}.png"

    
    def test_get_file_path(self):
        arquivo = get_file_path(None, 'teste.png')
        self.assertTrue(len(arquivo), len(self.filename))


class ServicoTestCase(TestCase):

    # Cria uma resposta assertiva, nesse caso, objetos da classe Servico
    def setUp(self):
        self.servico = mommy.make('Servico')

    
    # Cria uma execução teste, buscando comparar se a resposta assertiva é igual à uma execução normal da classe
    def test_str(self):
        self.assertEquals(str(self.servico), self.servico.servicos)


class CargoTestCase(TestCase):


    def setUp(self):
        self.cargo = mommy.make('Cargo')

    
    def test_str(self):
        self.assertEquals(str(self.cargo), self.cargo.cargo)


class FuncionarioTestCase(TestCase):


    def setUp(self):
        self.nome = mommy.make('Funcionario')

    
    def test_str(self):
        self.assertEquals(str(self.nome), self.nome.nome)


class Ferramentas1TestCase(TestCase):


    def setUp(self) -> None:
        self.titulo = mommy.make('Ferramentas1')

    
    def test_str(self):
        self.assertEquals(str(self.titulo), self.titulo.titulo)


class Ferramentas2TestCase(TestCase):


    def setUp(self) -> None:
        self.titulo = mommy.make('Ferramentas2')

    
    def test_str(self):
        self.assertEquals(str(self.titulo), self.titulo.titulo)


class TestemunhasTestCase(TestCase):


    def setUp(self) -> None:
        self.nome = mommy.make('Testemunhas')

    
    def test_str(self):
        self.assertEquals(str(self.nome), self.nome.nome)
        