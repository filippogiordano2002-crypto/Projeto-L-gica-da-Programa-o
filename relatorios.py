def relatorio_disponiveis(livros): # Apresenta uma relação com todos os livros disponíveis para empréstimo
    print("\n LIVROS DISPONÍVEIS: ")
    encontrou = False  # controla o loop para verificar se algum livro goi encontrado

    for livro in livros:
        if livro["status"] == "disponivel": # Verifica se o status do livro permite que seja emprestado
            print(f"ID: {livro['id']}, Título: {livro['titulo']}, Autor:{livro['autor']}")
            encontrou = True # Filtra os livros disponíveis e apresenta na tela

    if not encontrou:
        print("O livro não está disponível.") # Caso nenhum livro na lista esteja com status 'disponivel'


def relatorio_emprestados(livros, emprestimos, usuarios):
    print("\n LIVROS EMPRESTADOS")
    encontrou = False

    for livro in livros:
        if livro["status"] == "emprestado":
            encontrou = True # Apresenta os livros marccados como já emprestados

            nome_usuario = "Usuário desconhecido"
            data_emprestimo = "Data não encontrada" 

            for emprestimo in emprestimos: # Procura o empréstimo do livro
                if (emprestimo["id_livro"] == livro["id"] and emprestimo["data_devolucao"] == ""):
                    data_emprestimo = emprestimo["data_emprestimo"] # Procura o usuário que está com o livro

                    for user in usuarios:
                        if user["id"] == emprestimo["id_usuario"]:
                            nome_usuario = user["nome"]
                            break # Encerra a busca de usuários assim que forem encontrados
                    break  # Encerra a busca de empréstimos quando encontrdos

            print(f"ID: {livro['id']}, Título: {livro['titulo']}, Usuário:"f" {nome_usuario}, Data: {data_emprestimo}")

    if not encontrou:
        print("Nenhum registro de empréstimo encontrado.") # Caso nenhum livro na lista esteja com status 'emprestado'


def _exibir_usuarios_recursivo(usuarios, indice=0): # Função recursiva para percorrer a lista de usuários, apontando o primeiro item da lista
    if indice >= len(usuarios):
        return
    user = usuarios[indice]
    print(f"ID: {user['id']}, Nome: {user['nome']}")
    _exibir_usuarios_recursivo(usuarios, indice + 1) # Chama a função outra vez, mas adiciona mais um ao índice, para recomeçar a lista no próximo usuário


def relatorio_usuarios(usuarios):
    print("\n USUÁRIOS CADASTRADOS")
    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado.")
    else:
        _exibir_usuarios_recursivo(usuarios)
