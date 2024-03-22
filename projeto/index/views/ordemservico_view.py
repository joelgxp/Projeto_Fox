from django.shortcuts import render, redirect, get_object_or_404

from ..models import Veiculo, Servico, OrdemServico, OrdemServicoForm

def get_ordem_servico(request):
    ordemservico = OrdemServico.objects.all()
    return render(request, 'ordem-servico/ordem-servico.html', {'ordemservico': ordemservico})

def edit_ordem_servico(request, id):
    servicos = Servico.objects.filter(ordem_servico_id=id)
    ordemservico = OrdemServico.objects.get(id=id)
    print('veiculo: ', ordemservico)
    return render(request, 'ordem-servico/editar.html', {'servicos': servicos, 'ordemservico': ordemservico})

def create_ordem_servico(request):
    
    if request.method == 'POST':
        veiculo = request.POST.get('veiculo_id')
        print('veiculo: ', veiculo)
        veiculo_id = Veiculo.objects.get(id=veiculo)        
        print('veiculo_id: ', veiculo_id)
        
        nomes_itens = request.POST.getlist('servico')
        tempos_execucao = request.POST.getlist('tempo_execucao')
        valores = request.POST.getlist('valor')            
                
        formOrdemServico = OrdemServicoForm(request.POST)                
        
        if formOrdemServico.is_valid():
            ordem_servico = formOrdemServico.save(commit=False)
            ordem_servico.veiculo = veiculo_id
            ordem_servico.status = 1
            ordem_servico.save()   
            for nome, tempo_exec, valor in zip(nomes_itens, tempos_execucao, valores):
                Servico.objects.create(nome=nome, tempo_execucao=tempo_exec, valor=valor, ordem_servivo_id=ordem_servico.id)
            return redirect('criar_ordem_servico')
            
        else:
            print('erro do else', formOrdemServico.errors)    
    else:        
        formOrdemServico = OrdemServicoForm()
    return render(request, 'ordem-servico/criar.html', {'veiculos': Veiculo.objects.all()})
    
    


