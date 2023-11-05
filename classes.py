import mysql.connector
import datetime

class Pessoa:
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha
    
    def consultar_dados(self):
        # Conectar com banco de dados
        conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456',
        database= 'gfin',)

        cursor = conexao.cursor()

        id = self.id
        comando = f'SELECT descricao, valor, datas FROM tb_dados WHERE id_usuario = {id}'
        cursor.execute(comando)
        consulta = cursor.fetchall()
        if consulta == []:
            print('usuario sem dados! cadastre novos')
        else:
            print(consulta)

        cursor.close()
        conexao.close()


    def adicionar_dados(self):
        # Conectar com banco de dados
        conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456',
        database= 'gfin',)

        cursor = conexao.cursor()

        id = self.id
        descricao = input('\nInforme uma descrição: ').upper()
        valor = float(input('Digite um valor inteiro (obs: usar o sinal "-" para saídas): '))
        data = datetime.date.today()
        comando = 'INSERT INTO tb_dados (id_usuario, descricao, valor, datas) VALUES (%s, %s, %s, %s)'
        valores = (id, descricao, valor, data)
        cursor.execute(comando, valores)
        conexao.commit()
        print('\n------Salvo!------\n')


        cursor.close()
        conexao.close()
        
    
    def excluir_dados(self):
        # Conectar com banco de dados
        conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456',
        database= 'gfin',)

        cursor = conexao.cursor()

        #falta relacionar por id
        id = self.id
        comando = f'DELETE FROM tb_dados WHERE id_usuario = {id}'
        cursor.execute(comando)
        conexao.commit()
        print('\n------dados apagados!------\n')
        cursor.close()
        conexao.close()