# Módulo para o CRUD do main.py

"""
estrutura:
    {
        nome_da_tarefa: string
        descricao: string (max de 50 char)
        status: bool (true/false)
    }
"""
def adicionar_tarefa(nome, descricao): # Função para adicionar uma tarefa á lista.
    if not nome or not descricao:
        raise ValueError("Nome ou descrição estão faltando!")

    if len(descricao) > 50:
        raise ValueError("Máximo de caracteres em descrição foi antigido!")

    return {
        "nome_da_tarefa": nome,
        "descricao": descricao,
        "status": False
    }

def listar_tarefas(tarefas): # lista as tarefas ordenadamente.
    if not tarefas:
        print("\nSem tarefas cadastradas!\n")
    else:
        for idx, tarefa in enumerate(tarefas, 1):
            status = "Concluída" if tarefa["status"] else "Não concluída"

            print(f"{idx}. {tarefa["nome_da_tarefa"]} | {tarefa["descricao"]} | STATUS: {status}")

def concluir_tarefa(tarefas, indice):
    if indice < 0 or indice >= len(tarefas):
        raise IndexError("Indice inválido!")
    
    tarefas[indice]["status"] = True

def excluir_tarefa(tarefas, indice):
    if indice < 0 or indice >= len(tarefas):
        raise IndexError("Indice inválido!")

    tarefa_removida = tarefas.pop(indice)
    return tarefa_removida