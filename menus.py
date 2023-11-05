import getpass

def menu_inicio():
    op = input("""\n------BEM VINDO-------\n 
        \rE - ENTRAR
        \rC - CRIAR CONTA
        \rS - SAIR
        \r\nDigite uma opção: """).upper()
    return op

def menu_entrar():
    print('\n------ENTRAR------')
    usuario = input("""\nDIGITE: NOME DE USUARIO: """).upper
    senha = getpass.getpass("""DIGITE: SENHA: """)
    return (usuario, senha)

def menu_criar():
    print('\n------CADASTRO------')
    usuario = input('\nDIGITE UM NOME DE USUARIO: ').upper()
    senha = getpass.getpass('DIGITE UMA SENHA COM 4 DIGITOS: ')
    return (usuario, senha)


def menu_usuario():
    print('\n------gFin------')
    op = input("""\n 
        \rA - ADICIONAR
        \rE - EDITAR/EXCLUIR
        \rC - CONSULTAR
        \rS - SAIR
        \rDigite uma letra: """).upper()
    return op


def menu_adicionar():
    op = input("""\n------gFin-------\n 
        \rE - CADASTRAR ENTRADAS
        \rC - CADASTRAR SAIDAS
        \rS - SAIR
        \r\nDigite uma opção: """).upper()
    return op

def menu_editar():
    op = input("""\n------gFin-------\n 
        \rL - ALTERAR ENTRADAS
        \rC - ALTERAR SAIDAS
        \rC - EXCLUIR
        \rS - SAIR
        \r\nDigite uma opção: """).upper()
    return op


def menu_consultar():
    op = input("""\n------gFin-------\n 
        \rL - LISTAR ENTRADAS
        \rC - LISTAR SAIDAS
        \rS - SAIR
        \r\nDigite uma opção: """).upper()
    return op
