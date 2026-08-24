# Módulo para a organização do Main

def lin(char, qtd=30):
    print(char * qtd)

def tabela(menu):
    if isinstance(menu, dict):
        for nu, item in menu.items():
            print(f"{nu}. {item}")
    else:
        print("\nO objeto precisa ser um dicioário!\n")