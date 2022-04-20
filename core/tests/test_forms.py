from django.test import TestCase
from core.forms import ContatoForm


class ContatoFormTestCase(TestCase):


    def setUp(self):
        self.nome = 'Guilherme'
        self.email = 'email@gmail.com'
        self.assunto = 'Sobre as coisas que faltam xxx'
        self.mensagem = 'Blá blá blá blá'

        # Armazenando os dados em forma de dicionário
        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem,
        }

        # var form == Objeto "ContatoForm" onde tem o mesmo valor do dic self.dados
        self.form = ContatoForm(data=self.dados)

    
    def test_send_mail(self):
        formulario1 = ContatoForm(data=self.dados)
        formulario1.is_valid()
        enviar = formulario1.send_mail()

        formulario2 = self.form
        formulario2.is_valid()
        enviar2 = formulario2.send_mail()

        # Comparação entre os dois formulários enviados
        self.assertEquals(enviar, enviar2)
