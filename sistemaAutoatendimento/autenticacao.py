from config import conexao
from config.senhas import gerar_hash_senha

def cadastrar():
    conn = conexao.conectar()
    if conn:
        cursor = conn.cursor()
        try:
            nome = input("Digite o nome do usuário: ")
            email = input("Digite o email do usuário: ")
            senha = input("Digite a senha do usuário: ")

            if not nome.strip() or not email.strip() or not senha.strip():
                print("Nome, email e senha não podem estar vazios.")
                return

            cursor.execute("SELECT id FROM usuarios WHERE email = %s", (email,))
            if cursor.fetchone():
                print("Usuário já cadastrado.")
                return

            cursor.execute(
                "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)",
                (nome, email, gerar_hash_senha(senha)),
            )
            conn.commit()
            print("Usuário cadastrado com sucesso.")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Falha na conexão.")
        

def login():
    conn = conexao.conectar()
    if conn:
        cursor = conn.cursor()
        try:
            email = input("Digite o email do usuário: ")
            senha = input("Digite a senha do usuário: ")

            if not email.strip() or not senha.strip():
                print("Email e senha não podem estar vazios.")
                return

            cursor.execute(
                "SELECT id FROM usuarios WHERE email = %s AND senha = %s",
                (email, gerar_hash_senha(senha)),
            )
            usuario = cursor.fetchone()

            if not usuario:
                print("Email ou senha incorretos.")
                return

            return usuario[0]
        finally:
            cursor.close()
            conn.close()
    else:
        print("Falha na conexão.")