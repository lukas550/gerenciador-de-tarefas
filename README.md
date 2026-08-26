# Gerenciador de Tarefas

Aplicação de linha de comando (CLI) para gerenciamento de tarefas, desenvolvida em Python. O projeto permite adicionar, listar, concluir e excluir tarefas, com persistência local em arquivo de texto.

## Sobre o Projeto

O Gerenciador de Tarefas nasceu como um exercício de módulos e bibliotecas em Python e evoluiu para um projeto independente, com foco em organização de código, separação de responsabilidades e boas práticas de desenvolvimento.

O projeto é estruturado em pacotes, separando a lógica de negócio (manipulação de tarefas), a persistência de dados (leitura e escrita em arquivo) e a organização visual do menu em módulos independentes.

## Como Funciona

Ao iniciar a aplicação, o programa tenta carregar as tarefas previamente salvas no arquivo `tarefas.txt`. Caso o arquivo não exista, ele é criado automaticamente e a lista de tarefas inicia vazia.

O usuário interage com o sistema por meio de um menu numérico exibido no terminal, escolhendo uma das opções disponíveis. Ações que alteram os dados, como adicionar ou concluir uma tarefa, são persistidas automaticamente no arquivo de texto, garantindo que as informações não sejam perdidas ao encerrar o programa.

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

> O arquivo `tarefas.txt` é gerado automaticamente na primeira execução e não é versionado no repositório.

## Módulos e Funcionalidades

### main.py

Ponto de entrada da aplicação. Responsável por:

- Carregar as tarefas salvas ao iniciar o programa, tratando o caso em que o arquivo ainda não existe
- Exibir o menu principal em loop contínuo
- Capturar a escolha do usuário e direcionar para a função correspondente
- Tratar entradas inválidas exibindo mensagem de erro sem interromper a execução

### core/tarefas.py

Módulo responsável pela lógica de negócio relacionada às tarefas (CRUD). Cada tarefa é representada por um dicionário com a seguinte estrutura:

```python
{
    "nome_da_tarefa": str,
    "descricao": str,  # máximo de 50 caracteres
    "status": bool     # True para concluída, False para pendente
}
```

Funções do módulo:

- `adicionar_tarefa(nome, descricao)`: valida os dados de entrada e retorna um dicionário representando a nova tarefa. Lança `ValueError` caso o nome ou a descrição estejam vazios (incluindo strings com apenas espaços) ou caso a descrição ultrapasse 50 caracteres.
- `listar_tarefas(tarefas)`: recebe a lista de tarefas em memória e exibe cada uma numerada, com sua descrição e o status em texto (Concluída ou Não concluída). Caso a lista esteja vazia, informa que não há tarefas cadastradas.
- `concluir_tarefa(tarefas, indice)`: marca a tarefa no índice informado como concluída (status = True). Lança `IndexError` caso o índice seja inválido.
- `excluir_tarefa(tarefas, indice)`: remove a tarefa no índice informado da lista usando `pop()` e retorna a tarefa removida. Lança `IndexError` caso o índice seja inválido.

### core/arquivo.py

Módulo responsável pela persistência dos dados em arquivo de texto (`tarefas.txt`), mantendo as informações salvas entre execuções do programa.

Funções do módulo:

- `criar_arquivo()`: cria o arquivo `tarefas.txt` caso ele ainda não exista, evitando erros de leitura na primeira execução.
- `salvar_arquivo(tarefas, caminho)`: sobrescreve o arquivo com a lista de tarefas atual, uma tarefa por linha.
- `carregar_tarefas(caminho)`: lê o arquivo linha a linha e reconstrói a lista de dicionários de tarefas, convertendo o status salvo em texto de volta para valor booleano. Caso o arquivo não exista, a exceção `FileNotFoundError` é propagada para o chamador, que é responsável por tratá-la.

O formato de cada linha do arquivo segue o padrão:

```
Nome da Tarefa | Descrição da tarefa | Concluída
```

O campo de status é salvo como `Concluída` ou `Não Concluida`, mantendo o arquivo legível para leitura manual.

> Limitação conhecida: o separador ` | ` pode causar comportamento inesperado caso o nome ou a descrição da tarefa contenham essa sequência de caracteres. Será resolvido na migração para JSON.

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
- Manipulação de arquivos (leitura e escrita em `.txt`)
- Tratamento de exceções (`try/except/else`)
- Programação modular com pacotes e importações

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

## Autor

Feito com dedicação por Lukas.