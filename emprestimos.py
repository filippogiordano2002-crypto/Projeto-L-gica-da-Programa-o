from datetime import date

from usuarios import buscar_usuario


def emprestar_livro(livros, usuarios, emprestimos):
    #Registra o empréstimo de um livro ao usuário
    codigo = input('Código do livro: ').strip()
    matricula = input('Matrícula do usuário: ').strip()

    #Faz a verificação antes de fazer as alterações
    pos_livro = buscar_livro(livros, codigo)
    if pos_livro == -1:
        print('Livro não encontrado.')
        return False

    if livros[pos_livro][5] != 'disponivel':
        print('Esse livro já está emprestado.')
        return False

    pos_usuario = buscar_usuario(usuarios, matricula)
    if pos_usuario == -1:
        print('Usuário não encontrado.')
        return False
    
    #Altera os dados
    emprestimo = [codigo, matricula, str(date.today()), '']
    emprestimos.append(emprestimo)
    livros[pos_livro][5] = 'emprestado'

    salvar(ARQUIVO_LIVROS, livros)
    salvar(ARQUIVO_EMPRESTIMOS, emprestimos)
    print('Devolução registrada: ' livros[pos_livro][1])
    return True