function adicionarCampo() {
    // Criar o elemento div com a classe form-row
    var div = document.createElement("div");
    div.classList.add("form-row");

    // Criar o elemento div para cada campo em uma coluna
    var divNome = document.createElement("div");
    divNome.classList.add("form-group", "col-2");

    var divTempoExec = document.createElement("div");
    divTempoExec.classList.add("form-group", "col-2");

    var divValor = document.createElement("div");
    divValor.classList.add("form-group", "col-2");

    // Criar os rótulos e campos de entrada para cada campo
    var labelNome = document.createElement("label");
    labelNome.setAttribute("for", "nome_item");
    labelNome.textContent = "Serviço";
    var inputNome = document.createElement("input");
    inputNome.setAttribute("type", "text");
    inputNome.setAttribute("name", "nome_item");
    inputNome.classList.add("form-control");
    divNome.appendChild(labelNome);
    divNome.appendChild(inputNome);

    var labelTempoExec = document.createElement("label");
    labelTempoExec.setAttribute("for", "tempo_execucao");
    labelTempoExec.textContent = "Tempo de Execução";
    var inputTempoExec = document.createElement("input");
    inputTempoExec.setAttribute("type", "text");
    inputTempoExec.setAttribute("name", "tempo_execucao");
    inputTempoExec.classList.add("form-control");
    divTempoExec.appendChild(labelTempoExec);
    divTempoExec.appendChild(inputTempoExec);

    var labelValor = document.createElement("label");
    labelValor.setAttribute("for", "valor");
    labelValor.textContent = "Valor";
    var inputValor = document.createElement("input");
    inputValor.setAttribute("type", "text");
    inputValor.setAttribute("name", "valor");
    inputValor.classList.add("form-control");
    divValor.appendChild(labelValor);
    divValor.appendChild(inputValor);

    // Adicionar as divs dos campos à div principal
    div.appendChild(divNome);
    div.appendChild(divTempoExec);
    div.appendChild(divValor);

    // Adicionar a div principal ao elemento pai (por exemplo, ao formulário)
    var formGroup = document.getElementById("item-fields");
    formGroup.appendChild(div);
}
