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
        "tarefa": nome,
        "descricao": descricao,
        "status": False
    }

def listar_tarefas(): # lista as tarefas ordenadamente.
    pass # TODO: quando tiver uma persistência será feito.

def concluir_tarefa(tarefa):
    pass

def excluir_tarefa(tarefa):
    pass