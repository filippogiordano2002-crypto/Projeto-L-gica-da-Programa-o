from datetime import date

from arquivos import salvar
from livros import buscar_livro
from usuarios import buscar_usuario

ARQUIVO_LIVROS = 'livros.txt'
ARQUIVO_EMPRESTIMOS = 'emprestimos.txt'

# Formato dos registros (ordem fixa, igual ao documento):
# livro:      [codigo, titulo, autor, ano, genero, status]   -> status na posição 5
# empréstimo: [codigo_livro, matricula, data_emprestimo, data_devolucao]
#             data_devolucao fica '' enquanto o livro não foi devolvido


def emprestar_livro(livros, usuarios, emprestimos):
    # Registra o empréstimo de um livro a um usuário
    codigo = input('Código do livro: ').strip()
    matricula = input('Matrícula do usuário: ').strip()

    # Todas as verificações vêm ANTES de qualquer alteração
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

    # Tudo certo: agora sim altera os dados
    emprestimo = [codigo, matricula, str(date.today()), '']
    emprestimos.append(emprestimo)
    livros[pos_livro][5] = 'emprestado'

    salvar(ARQUIVO_LIVROS, livros)
    salvar(ARQUIVO_EMPRESTIMOS, emprestimos)
    print('Empréstimo registrado:', livros[pos_livro][1], 'para', usuarios[pos_usuario][1])
    return True


def devolver_livro(livros, emprestimos):
    # Registra a devolução de um livro
    codigo = input('Código do livro: ').strip()

    pos_livro = buscar_livro(livros, codigo)
    if pos_livro == -1:
        print('Livro não encontrado.')
        return False

    # Procura o empréstimo em aberto desse livro (data de devolução vazia)
    pos_emprestimo = -1
    for i in range(len(emprestimos)):
        if emprestimos[i][0] == codigo and emprestimos[i][3] == '':
            pos_emprestimo = i
            break

    if pos_emprestimo == -1:
        print('Esse livro não está emprestado.')
        return False

    emprestimos[pos_emprestimo][3] = str(date.today())
    livros[pos_livro][5] = 'disponivel'

    salvar(ARQUIVO_LIVROS, livros)
    salvar(ARQUIVO_EMPRESTIMOS, emprestimos)
    print('Devolução registrada:', livros[pos_livro][1])
    return True

