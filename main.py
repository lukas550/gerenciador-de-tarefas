from core.tarefas import (
    adicionar_tarefa, listar_tarefas, concluir_tarefa,
    excluir_tarefa
)
from core.arquivo import (
    salvar_arquivo, carregar_arquivo
)
from core.organizacao import (
    lin, tabela
)

menu = {
    "1": "Adicionar Tarefa",
    "2": "Listar Tarefas",
    "3": "Concluir Tarefa",
    "4": "Excluir Tarefa",
    "5": "Sair"
}

tarefas = carregar_arquivo()

lin("-")
tabela(menu)
lin("-")
print("Digite 'menu' para visualizar a tabela novamente!")

while True:
    print("\nDigite o número ou comando que deseja:")
    escolha = input("= ").lower().strip()

    if escolha == "menu":

        lin("-")
        tabela(menu)
        lin("-")

    elif escolha == "1":

        lin("-")
        try:
            nome_da_tarefa = input("Digite o nome da tarefa: ")
            descricao_da_tarefa = input(f"Digite a descrição da tarefa {nome_da_tarefa.capitalize()} (MAX 50 caracteres): ")

            tarefa = adicionar_tarefa(nome_da_tarefa, descricao_da_tarefa)
        except ValueError as e:
            print(f"\n{e}\n")

        else:
            tarefas.append(tarefa)
            salvar_arquivo(tarefas)

            print(f"\nTarefa {nome_da_tarefa.capitalize()} foi cadastrado!\n")
        lin("-")

    elif escolha == "2":
        pass

    elif escolha == "3":
        pass

    elif escolha == "4":
        pass

    elif escolha == "5":
        print("\nEncerrando...\n")
        break

    else:
        print("\nDigite algo válido!\n")