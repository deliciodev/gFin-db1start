import mysql.connector
from menus import menu_inicio, menu_entrar, menu_criar, menu_usuario
from bdados import validar_usuario, cadastrar_usuario
from classes import Pessoa
from getpass import getpass
import datetime


opt = ''

while opt != 'S':
    opt = menu_inicio()
    
    if opt == 'A':
        usuario, senha = menu_criar()
        cadastrar_usuario(usuario, senha)
    
    elif opt == 'B':
        usuario, senha = menu_entrar()
        pessoa = validar_usuario(usuario, senha)
        opt = menu_usuario()

        if opt == 'C':
            pessoa.consultar_dados()
            
        elif opt == 'D':
            pessoa.adicionar_dados()

            
        elif opt == 'E':
            pessoa.excluir_dados()
            
        else:
            break 
        
    print('\n------Volte Sempre!------\n')