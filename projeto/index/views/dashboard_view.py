from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ..models import Veiculo

@login_required
def get_veiculos(request):
    veiculos = Veiculo.objects.all()
    veiculos_oficina = Veiculo.objects.all().filter(status=1)
    veiculos_loja = Veiculo.objects.all().filter(status=0)
    return render(request, 'dashboard.html', {
        'veiculos': veiculos,
        'veiculos_oficina': veiculos_oficina,
        'veiculos_loja': veiculos_loja
        })