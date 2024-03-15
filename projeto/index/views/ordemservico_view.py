from django.shortcuts import render

from ..models import Veiculo

def get_ordem_servico(request):
    ordemservico = Veiculo.objects.all()
    return render(request, 'ordem-servico/ordem-servico.html', {'ordemservico': ordemservico})

def create_ordem_servico(request):
    return render(request, 'ordem-servico/criar.html')