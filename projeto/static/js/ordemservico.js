function adicionarCampo() {
    // Criar o elemento div
var div = document.createElement("div");
div.classList.add("form-group", "col-4");

// Criar o rótulo (label) para o nome
var labelNome = document.createElement("label");
labelNome.setAttribute("for", "nome_item");
labelNome.textContent = "Serviço";

// Criar o campo de entrada para o nome
var inputNome = document.createElement("input");
inputNome.setAttribute("type", "text");
inputNome.setAttribute("name", "nome_item");
inputNome.classList.add("form-control");

// Adicionar o rótulo e o campo de entrada para o nome à div
div.appendChild(labelNome);
div.appendChild(inputNome);

// Criar o rótulo (label) para o tempo de execução
var labelTempoExec = document.createElement("label");
labelTempoExec.setAttribute("for", "tempo_execucao");
labelTempoExec.textContent = "Tempo de Execução";

// Criar o campo de entrada para o tempo de execução
var inputTempoExec = document.createElement("input");
inputTempoExec.setAttribute("type", "text");
inputTempoExec.setAttribute("name", "tempo_execucao");
inputTempoExec.classList.add("form-control");

// Adicionar o rótulo e o campo de entrada para o tempo de execução à div
div.appendChild(labelTempoExec);
div.appendChild(inputTempoExec);

// Criar o rótulo (label) para o valor
var labelValor = document.createElement("label");
labelValor.setAttribute("for", "valor");
labelValor.textContent = "Valor";

// Criar o campo de entrada para o valor
var inputValor = document.createElement("input");
inputValor.setAttribute("type", "text");
inputValor.setAttribute("name", "valor");
inputValor.classList.add("form-control");

// Adicionar o rótulo e o campo de entrada para o valor à div
div.appendChild(labelValor);
div.appendChild(inputValor);

// Adicionar a div ao elemento pai (por exemplo, ao formulário)
var formGroup = document.getElementById("item-fields");
formGroup.appendChild(div);


}