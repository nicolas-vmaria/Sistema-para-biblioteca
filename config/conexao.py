import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'biblioteca'
}

def conectar():
    try:
        return mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuario ou senha inválidos.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Banco de dados não encontrado.")
        else:
            print(err)
        return None