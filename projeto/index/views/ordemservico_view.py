from django.shortcuts import render, redirect

from ..models import Veiculo, Servico

def get_ordem_servico(request):
    ordemservico = Veiculo.objects.all()
    return render(request, 'ordem-servico/ordem-servico.html', {'ordemservico': ordemservico})

def create_ordem_servico(request):
    if request.method == 'POST':
        nomes_itens = request.POST.getlist('nome_item')
        print(nomes_itens)
        
        novos_itens = []
        for nome_item in nomes_itens:
            novo_item = Servico.objects.create(nome=nome_item)
            novos_itens.append(novo_item)
        
        return redirect('ordem_servico')
    return render(request, 'ordem-servico/criar.html', {'veiculos': Veiculo.objects.all()})