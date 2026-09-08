# Gerenciador de Tarefas

Aplicação de linha de comando (CLI) para gerenciamento de tarefas, desenvolvida em Python. O projeto permite adicionar, listar, concluir e excluir tarefas, com persistência local em arquivo JSON.

## Sobre o Projeto

O Gerenciador de Tarefas nasceu como um exercício de módulos e bibliotecas em Python e evoluiu para um projeto independente, com foco em organização de código, separação de responsabilidades e boas práticas de desenvolvimento.

O projeto é estruturado em pacotes, separando a lógica de negócio (manipulação de tarefas), a persistência de dados (leitura e escrita em arquivo) e a organização visual do menu em módulos independentes.

## Como Funciona

Ao iniciar a aplicação, o programa carrega as tarefas previamente salvas no arquivo `tarefas.json`. Caso o arquivo não exista ou esteja corrompido, ele é recriado automaticamente e a lista de tarefas inicia vazia.

O usuário interage com o sistema por meio de um menu numérico exibido no terminal, podendo digitar o comando `menu` a qualquer momento para reexibi-lo. Ações que alteram os dados, como adicionar, concluir ou excluir uma tarefa, são persistidas automaticamente no arquivo JSON, garantindo que as informações não sejam perdidas ao encerrar o programa.

As operações de concluir e excluir são feitas por meio do nome da tarefa, em vez de um índice numérico, tornando a interação mais intuitiva. A exclusão exige confirmação explícita do usuário antes de ser efetivada.

## Estrutura do Projeto

```
gerenciador-de-tarefas/
├── core/
│   ├── __init__.py
│   ├── tarefas.py
│   ├── arquivo.py
│   └── organizacao.py
├── main.py
├── .gitignore
├── LICENSE
└── README.md
```

> O arquivo `tarefas.json` é gerado automaticamente na primeira execução e não é versionado no repositório.

## Módulos e Funcionalidades

### main.py

Ponto de entrada da aplicação. Responsável por:

- Carregar as tarefas salvas ao iniciar o programa
- Exibir o menu principal e permitir sua reexibição a qualquer momento pelo comando `menu`
- Capturar a escolha do usuário e direcionar para a função correspondente
- Solicitar confirmação do usuário antes de excluir uma tarefa
- Tratar entradas inválidas exibindo mensagem de erro sem interromper a execução

### core/tarefas.py

Módulo responsável pela lógica de negócio relacionada às tarefas (CRUD). Cada tarefa é representada por um dicionário com a seguinte estrutura:

```python
{
    "tarefa": str,      # nome da tarefa, normalizado em minúsculas
    "descricao": str,   # máximo de 50 caracteres
    "concluida": bool   # True para concluída, False para pendente
}
```

Funções do módulo:

- `adicionar_tarefa(nome, descricao)`: valida os dados de entrada e retorna um dicionário representando a nova tarefa. Lança `ValueError` caso o nome ou a descrição estejam vazios (incluindo strings com apenas espaços) ou caso a descrição ultrapasse 50 caracteres.
- `listar_tarefas(tarefas)`: recebe a lista de tarefas em memória e exibe cada uma com sua descrição e o status em texto (Concluída ou Não concluída). Caso a lista esteja vazia, informa que não há tarefas cadastradas.
- `concluir_tarefa(tarefa_a_concluir, tarefas)`: busca a tarefa pelo nome informado e marca como concluída (`concluida = True`). Lança `ValueError` caso a tarefa não seja encontrada.
- `excluir_tarefa(tarefa_a_excluir, tarefas)`: busca a tarefa pelo nome informado e a retorna, para que o chamador confirme e efetive a remoção da lista. Lança `ValueError` caso a tarefa não seja encontrada.

### core/arquivo.py

Módulo responsável pela persistência dos dados em arquivo JSON (`tarefas.json`), mantendo as informações salvas entre execuções do programa.

Funções do módulo:

- `salvar_arquivo(dados_a_salvar)`: sobrescreve o arquivo com a lista de tarefas atual, em formato JSON legível (`indent=4`). Trata erros de escrita (`OSError`) e de serialização (`TypeError`).
- `carregar_arquivo()`: lê o arquivo e reconstrói a lista de dicionários de tarefas. Caso o arquivo não exista, é criado automaticamente com uma lista vazia. Caso o conteúdo esteja corrompido, a exceção `json.JSONDecodeError` é tratada e a função retorna uma lista vazia.

A estrutura de cada tarefa no arquivo segue o formato:

```json
[
    {
        "tarefa": "estudar python",
        "descricao": "revisar módulos e bibliotecas",
        "concluida": false
    }
]
```

### core/organizacao.py

Módulo responsável pela organização visual da interface no terminal, mantendo o `main.py` mais limpo e focado no fluxo da aplicação.

Funções do módulo:

- `lin(char, qtd=30)`: imprime uma linha de separação visual, repetindo o caractere informado a quantidade de vezes especificada.
- `tabela(menu)`: recebe um dicionário e imprime cada par chave-valor formatado como item de menu numerado.

## Menu Principal

| Opção | Ação             |
|-------|------------------|
| 1     | Adicionar Tarefa |
| 2     | Listar Tarefas   |
| 3     | Concluir Tarefa  |
| 4     | Excluir Tarefa   |
| 5     | Sair             |

## Como Executar

1. Certifique-se de ter o Python 3 instalado.
2. Clone o repositório:

```
git clone https://github.com/lukas550/gerenciador-de-tarefas.git
```

3. Acesse a pasta do projeto:

```
cd gerenciador-de-tarefas
```

4. Execute o arquivo principal:

```
python main.py
```

## Tecnologias Utilizadas

- Python 3
- Manipulação de arquivos JSON
- Tratamento de exceções (`try/except/else`)
- Programação modular com pacotes e importações

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

## Autor

Feito com dedicação por Lukas.