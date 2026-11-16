def gerar_matricula(usuarios):
    return str(len(usuarios) + 1).zfill(3) #completa com zeros a esquerda ex: 001, 002


def buscar_usuario(usuarios, matricula):
    for i in range(len(usuarios)):
        if usuarios [i][0] == matricula:
            return i
    return -1
    #Devolve a posição do usuário na lista ou -1 se não existir


def cadastrar_usuario(usuarios):
    nome = input('Nome: ').strip()
    contato = input('Contato: ').strip()
# Pede nome e contato, gera a matrícula e adiciona à lista
    if nome == '' or contato == '':
        print('Nome e contato não podem ficar vazios.')
        return None


    matricula = gerar_matricula(usuarios)
    usuario = [matricula, nome, contato]
    usuarios.append(usuario)
    print(f'Usuário cadastrado com a matrícula {matricula}')
    return usuario


def listar_usuarios(usuarios):
    # Mostra todos os usuários cadastrados
    if len (usuarios) == 0:
        print('Nenhum usuario cadastrado.')
        return
    
    for usuario in usuarios:
        print(f'Matrícula: {usuario[0]} | Nome: {usuario[1]} | Contato: {usuario[2]}')