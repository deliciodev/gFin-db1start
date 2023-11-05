import getpass

def menu_inicio():
    op = input("""\n------BEM VINDO-------\n 
        \rA - CRIAR CONTA
        \rB - ENTRAR
        \rS - SAIR
        \r\nDigite uma opção: """).upper()
    return op

def menu_entrar():
    print('\n------ENTRAR------')
    usuario = input("""\nDIGITE: NOME DE USUARIO: """)
    senha = getpass.getpass("""DIGITE: SENHA: """)
    return (usuario, senha)

def menu_criar():
    print('\n------CADASTRO------')
    usuario = input('\nDIGITE UM NOME DE USUARIO: ')
    senha = getpass.getpass('DIGITE UMA SENHA COM 4 DIGITOS: ')
    return (usuario, senha)

def menu_usuario():
    print('\n------gFin------')
    op = input("""\n 
        \rC - CONSULTAR DADOS
        \rD - ADICIONAR DADOS
        \rE - EXCLUIR DADOS
        \rS - SAIR
        \r\nDigite uma letra: """).upper()
    return op
