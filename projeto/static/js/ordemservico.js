function add_servico(){

    container = document.getElementById("item-fields")

    html = `
    <br>
    <div class='row'> 
        <div class='col-5'> 
            <input type='text' placeholder='Serviço' class='form-control' name='servico'>
        </div> 
        <div class='col-md'>
            <input type='text' placeholder='Tempo de Execução' class='form-control' name='tempo_execucao'>
        </div> 
        <div class='col-md'>
            <input type='text' placeholder='Valor' class='form-control' name='valor'>
        </div> 
        <div class='col-md'>
        <button type="button" class="btn btn-primary" onclick="remove_servico(this)">Remover Item</button>
        </div>
        <div class='col-md'>
        <button type="button" class="btn btn-primary" onclick="add_servico()">Adicionar Item</button>
        </div>
    </div>
    <br>
    `

    container.insertAdjacentHTML('beforeend', html);

}

function remove_servico(button){
  var row = button.closest('.row');
  row.remove();
}

function disable_input_veiculo_data() {
    btn.getElementById("data_os").disabled = true;
    btn.getElementById("veiculo_select").disabled = true;
}