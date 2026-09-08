# Módulo para o CRUD do main.py

def adicionar_tarefa(nome, descricao): # Função para adicionar uma tarefa á lista.
    if not nome.strip() or not descricao.strip():
        raise ValueError("Nome ou descrição estão faltando!")

    if len(descricao) > 50:
        raise ValueError("Máximo de caracteres em descrição foi atingido!")

    return {
        "tarefa": nome.lower().strip(),
        "descricao": descricao,
        "concluida": False
    }

def listar_tarefas(tarefas): # lista as tarefas ordenadamente.
    if not tarefas:
        print("\nSem tarefas cadastradas!\n")
    else:
        for t in tarefas:
            status = "Concluida" if t["concluida"] else "Não concluida"
            print(f"- {t['tarefa'].capitalize()} - {t['descricao']} - Status: {status}")

def concluir_tarefa(tarefa_a_concluir, tarefas):
    # Busca
    encontrado = False
    for t in tarefas:
        if t["tarefa"].lower().strip() == tarefa_a_concluir.lower().strip():
            encontrado = True
            tarefa_encontrada = t
            break
    if not encontrado:
        raise ValueError(f"\nA tarefa {tarefa_a_concluir.capitalize()} não foi encontrada!\n")

    tarefa_encontrada['concluida'] = True

def excluir_tarefa(tarefa_a_excluir, tarefas):
    # Busca
    encontrado = False
    for t in tarefas:
        if t["tarefa"].lower().strip() == tarefa_a_excluir.lower().strip():
            encontrado = True
            tarefa_encontrada = t
            break
    if not encontrado:
        raise ValueError(f"\nA tarefa {tarefa_a_excluir.capitalize()} não foi encontrada!\n")

    return tarefa_encontrada