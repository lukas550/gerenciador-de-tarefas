# Módulo para salvar, carregar arquivos em .txt para a persistência.

def criar_arquivo():
    try:
        with open("tarefas.txt", "x", encoding="utf-8"):
            pass
    except FileExistsError:
        pass

def salvar_arquivo(tarefas, caminho="tarefas.txt"):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        for tarefa in tarefas:
            status = "Concluída" if tarefa["status"] else "Não Concluida"
            linha = f"{tarefa['nome_da_tarefa']} | {tarefa['descricao']} | {status}\n"

            arquivo.write(linha)

def carregar_tarefas(caminho="tarefas.txt"):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        tarefas = []

        for linha in arquivo:
            partes = linha.strip().split(" | ")
            if len(partes) == 3:
                tarefas.append({
                    "nome_da_tarefa": partes[0],
                    "descricao": partes[1],
                    "status": partes[2] == "Concluída"
                })

        return tarefas