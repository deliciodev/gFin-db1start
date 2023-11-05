import mysql.connector
from menus import menu_inicio, menu_entrar, menu_criar, menu_usuario
from getpass import getpass
from datetime import datetime
import json


opt = ''

while opt != 'S':
    opt = menu_inicio()
    
    if opt == 'E':
        menu_entrar()
    
    elif opt == 'C':
        menu_criar()
    else: 
        print('Volte Sempre!')