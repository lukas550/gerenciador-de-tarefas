# Módulo para salvar, carregar arquivos em .txt para a persistência.
import json

"""
estrutura do arquivo:
[
    {
        "tarefa": str,
        "descricao": str (máx 50 char),
        "concluida": bool    
    }
]
"""

ARQUIVO = "tarefas.json"

def salvar_arquivo(dados_a_salvar):
    try:
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            json.dump(dados_a_salvar, f, ensure_ascii=False, indent=4)

    except (OSError, TypeError) as e:
        print(f"\nErro no salvamento do arquivo: {e}")

def carregar_arquivo():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            dados = json.load(f)

            return dados
    except FileNotFoundError:
        salvar_arquivo([])

        return []

    except json.JSONDecodeError as e:
        print(f"\nErro em salvar o arquivo: {e}\n")

        return []