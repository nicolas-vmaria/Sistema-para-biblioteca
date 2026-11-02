from config import conexao

def adicionar_categoria():
    conn = conexao.conectar()
    if conn:
        categoria = input("Digite o nome da categoria: ").capitalize()
        
        if not categoria.strip():
            print("Nome da categoria não pode ser vazio.")
            conn.close()
            return
        
        cursor = conn.cursor()
        cursor.execute("Select * from categorias where nome = %s", (categoria,))
        
        if cursor.fetchone():
            print("Categoria já existe.")
        else:
            cursor.execute("INSERT INTO categorias (nome) VALUES (%s)", (categoria,))
            conn.commit()
            print("Categoria adicionada com sucesso.")
        cursor.close()
        conn.close()
    else:
        print("Falha na conexão.")
        

def listar_categorias():
    conn = conexao.conectar()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM categorias")
        categorias = cursor.fetchall()
        if not categorias:
            print("Nenhuma categoria encontrada.")
        else:
            for categoria in categorias:
                print(f"Nome: {categoria[1]}")
        cursor.close()
        conn.close()
    else:
        print("Falha na conexão.")
        
        
def atualizar_categoria():
    conn = conexao.conectar()
    if conn:
        nomeAntigo = input("Digite o nome da categoria que deseja atualizar: ").capitalize()
        if not nomeAntigo.strip():
            print("Nome da categoria não pode ser vazio.")
            conn.close()
            return

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM categorias WHERE nome = %s", (nomeAntigo,))
        categoria = cursor.fetchone()
        if categoria:
            nomeNovo = input ("Digite o novo nome da categoria: ").capitalize()
            if not nomeNovo.strip():
                print("Nome da categoria não pode ser vazio.")
            else:
                cursor.execute("UPDATE categorias SET nome = %s WHERE nome = %s", (nomeNovo, nomeAntigo))
                conn.commit()
                print("Categoria atualizada com sucesso.")
        else:
            print("Categoria não encontrada.")
        cursor.close()
        conn.close()
    else:
        print("Falha na conexão.")
        

def deletar_categoria():
    conn = conexao.conectar()
    if conn:
        nome = input("Digite o nome da categoria que deseja deletar: ").capitalize()
        if not nome.strip():
            print("Nome da categoria não pode ser vazio.")
            conn.close()
            return

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM categorias WHERE nome = %s", (nome,))
        categoria = cursor.fetchone()
        if categoria:
            cursor.execute("DELETE FROM categorias WHERE nome = %s", (nome,))
            conn.commit()
            print("Categoria deletada com sucesso.")
        else:
            print("Categoria não encontrada.")
        cursor.close()
        conn.close()
    else:
        print("Falha na conexão.")
        