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
        
        formOrdemServico = OrdemServicoForm(request.POST)                
        if formOrdemServico.is_valid():
            os = formOrdemServico.save(commit=False)
            os.veiculo = veiculo_id
            os.status = 1
            os.save()
        
        return insert_servico_os(request)
    return render(request, 'ordem-servico/criar.html', {'veiculos': Veiculo.objects.all()})


def insert_servico_os(request):
    servicos = []
    
    if request.method == 'POST':   
        
        nomes_itens = request.POST.getlist('servico')
        tempos_execucao = request.POST.getlist('tempo_execucao')
        valores = request.POST.getlist('valor')            
       
        for nome, tempo_exec, valor in zip(nomes_itens, tempos_execucao, valores):
            servico = Servico.objects.create(nome=nome, tempo_execucao=tempo_exec, valor=valor)
            servicos.append(servico)
            
        return redirect('criar_ordem_servico')
    
    return render(request, 'ordem-servico/criar.html')
    
    


