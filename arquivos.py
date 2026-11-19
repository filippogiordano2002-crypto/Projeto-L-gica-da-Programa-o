def carregar(nome_arquivo):
    # Lê um arquivo .txt e devolve uma lista de registros.
    # Recebe: o nome do arquivo (ex.: "livros.txt").
    # Devolve: lista de listas (um item por linha do arquivo).

    registros = []  # lista que vai guardar todos os registros

    try:
        # abre o arquivo para leitura ("r")
        arquivo = open(nome_arquivo, "r", encoding="utf-8")
    except FileNotFoundError:
        # se o arquivo não existe, devolve lista vazia em vez de dar erro
        return registros

    for linha in arquivo:  # percorre o arquivo linha por linha
        if linha.strip() != "":  # ignora linhas em branco
            # tira o \n do final e separa os campos pelo ";"
            registros.append(linha.strip().split(";"))

    arquivo.close()  # fecha o arquivo
    return registros


def salvar(nome_arquivo, registros):
    # Grava todos os registros no arquivo, substituindo o conteúdo antigo.
    # Recebe: o nome do arquivo e a lista de registros.

    # abre o arquivo para escrita ("w"): apaga o que havia antes
    arquivo = open(nome_arquivo, "w", encoding="utf-8")

    for registro in registros:
        # junta os campos com ";" e adiciona a quebra de linha
        arquivo.write(";".join(registro) + "\n")

    arquivo.close()  # fecha o arquivo (garante que tudo foi gravado)