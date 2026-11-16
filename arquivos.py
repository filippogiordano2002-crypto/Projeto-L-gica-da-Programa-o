def carregar(nome_arquivo):
    
    registros = []
    try:
        arquivo = open(nome_arquivo, "r", encoding="utf-8")
    except FileNotFoundError:
        return registros

    for linha in arquivo:
        if linha.strip() != "":
            registros.append(linha.strip().split(";"))
    arquivo.close()
    return registros


def salvar(nome_arquivo, registros):
    
    arquivo = open(nome_arquivo, "w", encoding="utf-8")
    for registro in registros:
        arquivo.write(";".join(registro) + "\n")
    arquivo.close()