from arquivos import salvar  # função que grava a lista no arquivo


def buscar_livro(livros, codigo, posicao=0):
    # Procura um livro pelo código, de forma recursiva.
    # Recebe: a lista de livros, o código procurado e a posição atual.
    # Devolve: a posição do livro na lista, ou -1 se não existir.

    # caso base 1: chegou ao fim da lista sem encontrar
    if posicao == len(livros):
        return -1

    # caso base 2: o código do livro atual é o procurado
    if livros[posicao][0] == codigo:
        return posicao

    # caso recursivo: não achou aqui, então procura na próxima posição
    return buscar_livro(livros, codigo, posicao + 1)


def cadastrar_livro(livros):
    # Pede os dados de um livro, valida e cadastra.
    # Recebe: a lista de livros (que será alterada e salva).

    # pede os dados e remove espaços das pontas com strip()
    codigo = input("Código: ").strip()
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    ano = input("Ano: ").strip()
    genero = input("Gênero: ").strip()

    # validação 1: nenhum campo pode estar vazio
    if "" in [codigo, titulo, autor, ano, genero]:
        print("Erro: todos os campos são obrigatórios.")
    # validação 2: o ano deve ter apenas números
    elif not ano.isdigit():
        print("Erro: o ano deve conter apenas números.")
    # validação 3: o código não pode já existir (usa a busca recursiva)
    elif buscar_livro(livros, codigo) != -1:
        print("Erro: já existe um livro com esse código.")
    else:
        # tudo certo: adiciona o livro com status inicial "disponivel"
        livros.append([codigo, titulo, autor, ano, genero, "disponivel"])
        salvar("livros.txt", livros)  # grava no arquivo
        print("Livro cadastrado com sucesso!")


def listar_livros(livros):
    # Mostra todos os livros cadastrados, um por linha.
    # Recebe: a lista de livros.

    # se a lista está vazia, avisa o usuário
    if len(livros) == 0:
        print("Nenhum livro cadastrado.")

    # mostra cada livro com os campos separados por " - "
    for livro in livros:
        print(" - ".join(livro))