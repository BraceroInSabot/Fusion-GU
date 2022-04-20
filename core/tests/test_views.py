from django.test import TestCase, Client
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):


    def setUp(self):
        self.dados = {
            'nome': 'Guilherme',
            'email': 'email@gmail.com',
            'assunto': 'Assunto muito interessante sobre X coisa',
            'mensagem': 'Muitas coisas sendo faladas, importantes etc...',
        }
        self.cliente = Client()


    def test_form_valid(self):
        # Requisitando um método post para rota index usando os dados do dic acima
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        # Quando realizado, o método post retorna para a página index, o código "302" significa um redirect
        self.assertEqual(request.status_code, 302)

    
    def test_form_invalid(self):
        # Primeiro passo: deixar dados inválidos:
        dados = {
            'nome': 'Guilherme',
            'mensagem': 'AAAAAAAAA',
        }
        # Repetimos o código
        request = self.cliente.post(reverse_lazy('index'), data=dados)
        self.assertEquals(request.status_code, 200)