from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Servico, Funcionario, Ferramentas1, Ferramentas2, Testemunhas
from .forms import ContatoForm

class IndexView(FormView):
    template_name = "index.html"
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        ctx = super(IndexView, self).get_context_data(**kwargs)
        ctx['servicos'] = Servico.objects.order_by('?').all() # Buscando do banco de dados
        ctx['funcionarios'] = Funcionario.objects.all()
        ctx['ferramenta1'] = Ferramentas1.objects.order_by('?').all()
        ctx['ferramenta2'] = Ferramentas2.objects.order_by('?').all()
        ctx['testemunhas'] = Testemunhas.objects.order_by('?').all()
        return ctx

    
    # As duas funções derivam do FormView, que foi importado na linha 2

    # Caso a mensagem seja enviada:
    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    
    # Caso a mensagem NÃO seja enviada:
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro no envio do E-mail.')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)