# Menu principal do sistema de gerenciamento de biblioteca.

from arquivos import carregar, salvar
from livros import cadastrar_livro, listar_livros
from usuarios import cadastrar_usuario, listar_usuarios
from emprestimos import emprestar_livro, devolver_livro
from relatorios import (
    relatorio_disponiveis,
    relatorio_emprestados,
    relatorio_usuarios
)


def mostrar_menu():
    # Exibe as opcoes principais do sistema.
    print("\n========== BIBLIOTECA ==========")
    print("1 - Cadastrar livro")
    print("2 - Cadastrar usuario")
    print("3 - Emprestar livro")
    print("4 - Devolver livro")
    print("5 - Listar livros")
    print("6 - Listar usuarios")
    print("7 - Relatorios")
    print("0 - Sair")
    print("================================")


def menu_relatorios(livros, emprestimos, usuarios):
    # Converte as listas em dicionarios para utilizar os relatorios.

    livros_relatorio = []

    for livro in livros:
        livros_relatorio.append({
            "id": livro[0],
            "titulo": livro[1],
            "autor": livro[2],
            "status": livro[5]
        })

    usuarios_relatorio = []

    for usuario in usuarios:
        usuarios_relatorio.append({
            "id": usuario[0],
            "nome": usuario[1]
        })

    emprestimos_relatorio = []

    for emprestimo in emprestimos:
        emprestimos_relatorio.append({
            "id_livro": emprestimo[0],
            "id_usuario": emprestimo[1],
            "data_emprestimo": emprestimo[2],
            "data_devolucao": emprestimo[3]
        })

    # Mostra as opcoes de relatorios.
    print("\n---------- RELATORIOS ----------")
    print("1 - Livros disponiveis")
    print("2 - Livros emprestados")
    print("3 - Usuarios cadastrados")

    opcao = input("Escolha um relatorio: ").strip()

    if opcao == "1":
        relatorio_disponiveis(livros_relatorio)

    elif opcao == "2":
        relatorio_emprestados(
            livros_relatorio,
            emprestimos_relatorio,
            usuarios_relatorio
        )

    elif opcao == "3":
        relatorio_usuarios(usuarios_relatorio)

    else:
        print("Opcao de relatorio invalida.")


def main():
    # Carrega os dados salvos nos arquivos TXT.
    livros = carregar("livros.txt")
    usuarios = carregar("usuarios.txt")
    emprestimos = carregar("emprestimos.txt")

    while True:
        mostrar_menu()

        opcao = input("Digite uma opcao: ").strip()

        if opcao == "1":
            cadastrar_livro(livros)

        elif opcao == "2":
            cadastrar_usuario(usuarios)
            salvar("usuarios.txt", usuarios)

        elif opcao == "3":
            emprestar_livro(livros, usuarios, emprestimos)

        elif opcao == "4":
            devolver_livro(livros, emprestimos)

        elif opcao == "5":
            listar_livros(livros)

        elif opcao == "6":
            listar_usuarios(usuarios)

        elif opcao == "7":
            menu_relatorios(livros, emprestimos, usuarios)

        elif opcao == "0":
            print("Sistema encerrado. Ate mais!")
            break

        else:
            print("Opcao invalida. Tente novamente.")


if __name__ == "__main__":
    main()
