from config import conexao
from config.senhas import gerar_hash_senha
from mysql.connector import IntegrityError

def adicionar_usuario():
    conn = conexao.conectar()
    if conn:
        nome = input("Digite o nome do usuário: ")
        email = input("Digite o email do usuário: ")
        senha = input("Digite a senha do usuário: ")

        if not nome.strip():
            print("Nome do usuário não pode ser vazio.")
            conn.close()
            return
        if not email.strip():
            print("Email do usuário não pode ser vazio.")
            conn.close()
            return
        if not senha.strip():
            print("Senha do usuário não pode ser vazia.")
            conn.close()
            return
        senha = gerar_hash_senha(senha)
        
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        email_existente = cursor.fetchone()
        if email_existente:
            print("Erro: O email já está em uso. Por favor, escolha outro email.")
            cursor.close()
            conn.close()
            return
        
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)", (nome, email, senha))
        conn.commit()
        print("Usuário adicionado com sucesso.")
        cursor.close()
        conn.close()
    else:
        print("Falha na conexão.")
        

def listar_usuarios():
    conn = conexao.conectar()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, email FROM usuarios")
        usuarios = cursor.fetchall()
        if not usuarios:
            print("Nenhum usuário encontrado.")
        else:
            print("\nLista de Usuários:")
            for usuario in usuarios:
                print(f"ID: {usuario[0]}, Nome: {usuario[1]}, Email: {usuario[2]}")
        cursor.close()
        conn.close()
    else:
        print("Falha na conexão.")
        

def atualizar_usuario():
    conn = conexao.conectar()
    if conn:
        id_usuario = input("Digite o ID do usuário que deseja atualizar: ")
        if not id_usuario.strip():
            print("ID do usuário não pode ser vazio.")
            conn.close()
            return

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id_usuario,))
        usuario = cursor.fetchone()
        
        if usuario:
            novo_nome = input(f"Digite o novo nome (atual: {usuario[1]}): ") or usuario[1]
            novo_email = input(f"Digite o novo email (atual: {usuario[2]}): ") or usuario[2]
            nova_senha = input("Digite a nova senha (deixe em branco para não alterar): ")
            if nova_senha:
                nova_senha = gerar_hash_senha(nova_senha)
            else:
                nova_senha = usuario[3]  # Mantém a senha atual
            
            cursor.execute("UPDATE usuarios SET nome = %s, email = %s, senha = %s WHERE id = %s",
                           (novo_nome, novo_email, nova_senha, id_usuario))
            conn.commit()
            print("Usuário atualizado com sucesso.")
        else:
            print("Usuário não encontrado.")
        
        cursor.close()
        conn.close()
    else:
        print("Falha na conexão.")
        
        
def deletar_usuario():
    conn = conexao.conectar()
    if conn:
        id_usuario = input("Digite o ID do usuário que deseja deletar: ")
        if not id_usuario.strip():
            print("ID do usuário não pode ser vazio.")
            conn.close()
            return

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id_usuario,))
        usuario = cursor.fetchone()
        
        if usuario:
            confirmacao = input(f"Tem certeza que deseja deletar o usuário {usuario[1]}? (s/n): ")
            if confirmacao.lower() == 's':
                try:
                    cursor.execute("DELETE FROM usuarios WHERE id = %s", (id_usuario,))
                    conn.commit()
                    print("Usuário deletado com sucesso.")
                except IntegrityError:
                    conn.rollback()
                    print("Não é possível excluir o usuário porque há empréstimos associados.")
            else:
                print("Operação cancelada.")
        else:
            print("Usuário não encontrado.")
        
        cursor.close()
        conn.close()
    else:
        print("Falha na conexão.")