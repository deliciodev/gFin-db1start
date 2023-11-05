import mysql.connector
from classes import Pessoa


def cadastrar_usuario(usuario, senha):
    # Conectar com banco de dados
    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database= 'gfin',)
    
    cursor = conexao.cursor()

    nome = usuario
    senha = senha

    # Create
    comando = f'INSERT INTO tb_usuarios (nome, senha) VALUES ("{nome}", {senha})'
    cursor.execute(comando)
    conexao.commit()
    print("\nUsuário Cadastrado com sucesso!")
    print("Agora você pode ENTRAR!")


    cursor.close()
    conexao.close()


def validar_usuario(usuario, senha):
      # Conectar com banco de dados
      conexao = mysql.connector.connect(
      host='localhost',
      user='root',
      password='123456',
      database= 'gfin',)

      cursor = conexao.cursor()

      idUsuario = None
      nome = usuario
      senha = senha
      #Read
      comando = f'SELECT id_usuario FROM tb_usuarios WHERE nome = "{nome}" AND senha = {senha}'
      cursor.execute(comando)
      resultado = cursor.fetchone() #ler bd

      if resultado:
          idUsuario = resultado[0]
          print(f'\nLogin válidado!\n')
          cursor.close()
          conexao.close()
      
      else:
           print('\nCredenciais invalidas, Tente novamente\n')

      return Pessoa(idUsuario, nome, senha)