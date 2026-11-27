# Sistema de Gerenciamento de Biblioteca

Sistema de biblioteca feito em Python, que roda no terminal e guarda todos os dados em arquivos de texto (`.txt`). Desenvolvido em grupo como trabalho da faculdade.

## Funcionalidades

- Cadastro de livros (código, título, autor, ano e gênero)
- Cadastro de usuários (matrícula gerada automaticamente no formato `001`, `002`...)
- Empréstimo e devolução de livros
- Listagem de livros e de usuários
- Relatórios: livros disponíveis, livros emprestados (com o usuário e a data) e usuários cadastrados
- Dados salvos em arquivos, então nada se perde ao fechar o programa

## Como executar

Na pasta do projeto, rode:

```
main.py
```

Os arquivos de dados (`livros.txt`, `usuarios.txt` e `emprestimos.txt`) são criados automaticamente na pasta onde o programa é executado, na primeira vez que algo é cadastrado.

## Menu principal

| Opção | O que faz |
|---|---|
| 1 | Cadastrar livro |
| 2 | Cadastrar usuário |
| 3 | Emprestar livro |
| 4 | Devolver livro |
| 5 | Listar livros |
| 6 | Listar usuários |
| 7 | Relatórios |
| 0 | Sair |

## Estrutura dos arquivos

| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Menu principal; carrega os dados ao iniciar e chama as funções |
| `arquivos.py` | Funções `carregar` e `salvar` para ler e gravar os `.txt` |
| `livros.py` | Cadastro, busca (recursiva) e listagem de livros |
| `usuarios.py` | Cadastro, busca e listagem de usuários |
| `emprestimos.py` | Empréstimo e devolução de livros |
| `relatorios.py` | Relatórios de disponíveis, emprestados e usuários |

## Formato dos dados

Cada arquivo guarda um registro por linha, com os campos separados por `;`. Por isso, o símbolo `;` não deve ser usado nos campos de texto.

**`livros.txt`:** código; título; autor; ano; gênero; status (`disponivel` ou `emprestado`)

```
101;Dom Casmurro;Machado de Assis;1899;Romance;disponivel
```

**`usuarios.txt`:** matrícula; nome; contato

```
001;Ana;ana@email.com
```

**`emprestimos.txt`:** código do livro; matrícula; data do empréstimo; data da devolução (vazia enquanto o livro não foi devolvido)

```
101;001;2026-11-26;
102;001;2026-10-01;2026-10-15
```

## Conceitos utilizados

- Funções para modularizar o código
- Recursividade (`buscar_livro` em `livros.py` e a exibição de usuários em `relatorios.py`)
- Manipulação de arquivos para armazenar os dados

## Integrantes e responsabilidades

| Integrante | Responsável por |
|---|---|
| Filippo | `usuarios.py` e `emprestimos.py` |
| Julia | `main.py` e `relatorios.py` |
| Gideão | `main.py` e `relatorios.py` |
| Kennedy | `arquivos.py` e `livros.py` |
