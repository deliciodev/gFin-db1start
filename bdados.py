import mysql.connector


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
    print("Usuário Cadastrado com sucesso!")


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

      nome = usuario
      senha = senha
      #Read
      comando = f'SELECT id_usuario FROM tb_usuarios WHERE nome = "{nome}" AND senha = {senha}'
      cursor.execute(comando)
      resultado = cursor.fetchone() #ler bd

      if resultado:
           idUsuario = resultado[0]
           print(f'Login válido. id: {idUsuario}')
      else:
           print('Credenciais invalidas')

    
      cursor.close()
      conexao.close()
      return idUsuario


#Update
#comando = f'UPDATE tb_usuarios SET senha = {senha} WHERE nome = "{nome}"'
#cursor.execute(comando)
#conexao.commit() # edita o bd


#Delete
#comando = f'DELETE FROM tb_usuarios WHERE nome = "{nome}"'
#cursor.execute(comando)
#conexao.commit() # exclui o dado da tabela


#cursor.close()
#conexao.close()