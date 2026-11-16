from arquivos import salvar


def buscar_livro(livros, codigo, posicao=0):
    
    if posicao == len(livros):
        return -1
    if livros[posicao][0] == codigo:
        return posicao
    return buscar_livro(livros, codigo, posicao + 1)


def cadastrar_livro(livros):
    
    codigo = input("Código: ").strip()
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    ano = input("Ano: ").strip()
    genero = input("Gênero: ").strip()

    if "" in [codigo, titulo, autor, ano, genero]:
        print("Erro: todos os campos são obrigatórios.")
    elif not ano.isdigit():
        print("Erro: o ano deve conter apenas números.")
    elif buscar_livro(livros, codigo) != -1:
        print("Erro: já existe um livro com esse código.")
    else:
        livros.append([codigo, titulo, autor, ano, genero, "disponivel"])
        salvar("livros.txt", livros)
        print("Livro cadastrado com sucesso!")


def listar_livros(livros):
    
    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
    for livro in livros:
        print(" - ".join(livro))