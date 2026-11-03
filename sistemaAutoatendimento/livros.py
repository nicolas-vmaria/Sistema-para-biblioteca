from config import conexao

def listar_livros():
    conn = conexao.conectar()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM livros")
        livros = cursor.fetchall()
        if not livros:
            print("Nenhum livro encontrado.")
        else:
            for livro in livros:
                print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}")
        cursor.close()
        conn.close()
    else:
        print("Falha na conexão.")