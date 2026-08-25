from core import tarefas
from core import organizacao
from core import arquivo

menu = {
    "1": "Adicionar Tarefa",
    "2": "Listar Tarefas",
    "3": "Concluir Tarefa",
    "4": "Excluir Tarefa",
    "5": "Sair"
}

try:
    lista_tarefas = arquivo.carregar_tarefas()
except FileNotFoundError:
    arquivo.criar_arquivo()
    lista_tarefas = []
while True:
    organizacao.lin("-")
    organizacao.tabela(menu)
    organizacao.lin("-")

    escolha = input("Digite o número da opção que deseja: ").strip()

    if escolha == "1":

        organizacao.lin("-")
        try:
            nome_da_tarefa = input("Digite o nome da tarefa: ")
            descricao_da_tarefa = input("Digite a descrição da tarefas:")

            tarefa = tarefas.adicionar_tarefa(nome_da_tarefa, descricao_da_tarefa)
        except ValueError as e:
            print(f"\n{e}\n")
        else:
            lista_tarefas.append(tarefa)
            arquivo.salvar_arquivo(lista_tarefas)

            print("\nTarefa salva com sucesso!\n")
        organizacao.lin("-")

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
        print("\nDigite uma opção válida!\n")