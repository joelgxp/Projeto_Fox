from django.shortcuts import render, redirect, get_object_or_404

from ..models import Veiculo, Servico, OrdemServico

def get_ordem_servico(request):
    ordemservico = OrdemServico.objects.all()
    return render(request, 'ordem-servico/ordem-servico.html', {'ordemservico': ordemservico})

def create_ordem_servico(request):
    
    if request.method == 'POST':
        placa_veiculo = request.POST.get('veiculo')
        veiculo_id = get_object_or_404(Veiculo, placa=placa_veiculo).id
        
        nomes_itens = request.POST.getlist('nome_item')
        tempos_execucao = request.POST.getlist('tempo_execucao')
        valores = request.POST.getlist('valor')
        
        novos_itens = []
        for nome, tempo_exec, valor in zip(nomes_itens, tempos_execucao, valores):
            novo_item = Servico.objects.create(nome=nome, tempo_execucao=tempo_exec, valor=valor, id_veiculo_id=veiculo_id)
            novos_itens.append(novo_item)
            
            
            
        print(novos_itens)
        print(nomes_itens, tempos_execucao, valores)
        
        return redirect('criar_ordem_servico')
    
    return render(request, 'ordem-servico/criar.html', {'veiculos': Veiculo.objects.all(), 'itens': Servico.objects.all()})


