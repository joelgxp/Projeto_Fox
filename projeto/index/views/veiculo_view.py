from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from ..models import Veiculo, VeiculoForm

@login_required
def get_veiculos(request):
    veiculos = Veiculo.objects.all()    
    return render(request, 'veiculo/veiculo.html', {'veiculos': veiculos})

@login_required
def get_veiculo(request, placa):
    veiculo = Veiculo.objects.get(placa=placa)
    return render(request, 'veiculo/veiculo.html', {'veiculo': veiculo})

@login_required
def create_veiculo(request):
    
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('veiculos'))
        else:
            print('erro')
    else:
        form = VeiculoForm()
        
    return render(request, 'veiculo/cadastro.html', {'form': form})

@login_required
def update_veiculo(request, id):
    veiculo = Veiculo.objects.get(id=id)
    
    if request.method == 'POST':
        form = VeiculoForm(request.POST, instance=veiculo)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('veiculos'))
        else:            
            print('erro')
    else:
        form = VeiculoForm(instance=veiculo)
    return render(request, 'veiculo/editar.html', {'form': form, 'veiculo': veiculo})