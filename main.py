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
lista_tarefas = [

]

try:
    arquivo_salvo = arquivo.carregar_tarefas()

    for item in arquivo_salvo:
        lista_tarefas.append(item)
except FileNotFoundError:
    arquivo.criar_arquivo()

while True:
    organizacao.lin("-")
    organizacao.tabela(menu)
    organizacao.lin("-")

    escolha = input("Digite o número da opção que deseja: ").strip()

    if escolha == "1":
        pass
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