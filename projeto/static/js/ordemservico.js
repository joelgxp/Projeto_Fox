function adicionarCampo() {
    var container = document.getElementById("item-fields");
    var nome = document.createElement("input");
    var tempoExec = document.createElement("input");
    var valor = document.createElement("input");

    nome.type = "text";
    nome.name = "nome_item";
    tempoExec.type = "number";
    tempoExec.name = "tempoExec_item";
    valor.type = "number";
    valor.name = "valor_item";

    container.appendChild(nome);
    container.appendChild(tempoExec);
    container.appendChild(valor);
}