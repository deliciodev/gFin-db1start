# implementar condicao para sair do app
def cabecalho():
    return print('\nPara sair a qualquer momento pressione a letra: Q')

def menu_criar_login():
    usuario = input("""\nDIGITE UM NOME DE USUARIO: """).upper
    senha = input("""\nDIGITE UM NOME DE SENHA: """).upper
    return (usuario, senha)
    
def menu_usuario():
    op = input("""\n 
        \rA - ADICIONAR
        \rE - EDITAR/EXCLUIR
        \rC - CONSULTAR
        \rS - SAIR
        \rDigite uma letra: """).upper()
    return op


def menu_adicionar():
    op = input("""\n\rE - CADASTRAR ENTRADAS
                  \rS - CADASTRAR SAIDAS 
                  \n\rDigite uma letra: """).upper()
    return op

def menu_editar():
    # imprimir lista para usuario escolher onde alterar
    op = input("""\n\rDigite o ID: """).upper()
    return op

def menu_consultar():
    # imprimir lista para usuario escolher onde alterar
    op = input("""\n\rZ - Extrato por dia
                  \rW - Extrato completo
                  \n\rDigite uma letra: """).upper()
    return op
