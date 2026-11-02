from config import conexao

def adicionar_livro():
    conn = conexao.conectar()
    if conn:
        cursor = conn.cursor()
        nome = input("Digite o nome do livro: ").capitalize()
        autor = input("Digite o autor do livro: ").title()
        categoria = input("Digite o nome da categoria do livro: ").capitalize()
        quantidade = input("Digite a quantidade de exemplares do livro: ")

        if not nome.strip():
            print("Nome do livro não pode ser vazio.")
            cursor.close()
            conn.close()
            return
        if not autor.strip():
            print("Autor do livro não pode ser vazio.")
            cursor.close()
            conn.close()
            return
        if not categoria.strip():
            print("Nome da categoria não pode ser vazio.")
            cursor.close()
            conn.close()
            return
        if not quantidade.strip():
            print("Quantidade de exemplares não pode ser vazia.")
            cursor.close()
            conn.close()
            return
    
        cursor.execute("SELECT * FROM livros WHERE titulo = %s", (nome,))
        livro_existente = cursor.fetchone()
        
        cursor.execute("SELECT * FROM categorias WHERE nome = %s", (categoria,))
        categoria_existente = cursor.fetchone()
    
        if livro_existente:
            print("Livro já cadastrado.")
        elif not categoria_existente:
            print("Categoria não encontrada.")
        else:
            cursor.execute("Insert into livros (titulo, autor, categoria_id, quantidade) values (%s, %s, (select id from categorias where nome = %s), %s)", (nome, autor, categoria, quantidade))
            conn.commit()
        cursor.close()
        conn.close()
    else:
        print("Falha na conexão.")
        

def listar_livros():
    conn = conexao.conectar()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT l.titulo, l.autor, c.nome, l.quantidade FROM livros l JOIN categorias c ON l.categoria_id = c.id")
        livros = cursor.fetchall()
        if not livros:
            print("Nenhum livro encontrado.")
        else:
            for livro in livros:
                print(f"Título: {livro[0]}, Autor: {livro[1]}, Categoria: {livro[2]}, Quantidade: {livro[3]}")
        cursor.close()
        conn.close()
    else:
        print("Falha na conexão.")
        

def atualizar_livro():
    conn = conexao.conectar()
    if conn:
        cursor = conn.cursor()
        nome_antigo = input("Digite o nome do livro que deseja atualizar: ").capitalize()
        if not nome_antigo.strip():
            print("Nome do livro não pode ser vazio.")
            cursor.close()
            conn.close()
            return

        cursor.execute("SELECT * FROM livros WHERE titulo = %s", (nome_antigo,))
        livro_existente = cursor.fetchone()
        
        if livro_existente:
            nome_novo = input("Digite o novo nome do livro: ").capitalize()
            autor_novo = input("Digite o novo autor do livro: ").title()
            categoria_nova = input("Digite a nova categoria do livro: ").capitalize()
            quantidade_nova = input("Digite a nova quantidade de exemplares do livro: ")

            if not nome_novo.strip():
                print("Nome do livro não pode ser vazio.")
                cursor.close()
                conn.close()
                return
            if not autor_novo.strip():
                print("Autor do livro não pode ser vazio.")
                cursor.close()
                conn.close()
                return
            if not categoria_nova.strip():
                print("Nome da categoria não pode ser vazio.")
                cursor.close()
                conn.close()
                return
            if not quantidade_nova.strip():
                print("Quantidade de exemplares não pode ser vazia.")
                cursor.close()
                conn.close()
                return
            
            cursor.execute("SELECT * FROM categorias WHERE nome = %s", (categoria_nova,))
            categoria_existente = cursor.fetchone()
            
            if not categoria_existente:
                print("Categoria não encontrada.")
            else:
                cursor.execute("UPDATE livros SET titulo = %s, autor = %s, categoria_id = (SELECT id FROM categorias WHERE nome = %s), quantidade = %s WHERE titulo = %s", (nome_novo, autor_novo, categoria_nova, quantidade_nova, nome_antigo))
                conn.commit()
                print("Livro atualizado com sucesso.")
        else:
            print("Livro não encontrado.")
        
        cursor.close()
        conn.close()
    else:
        print("Falha na conexão.")
        
        
def deletar_livro():
    conn = conexao.conectar()
    if conn:
        cursor = conn.cursor()
        nome = input("Digite o nome do livro que deseja deletar: ").capitalize()
        if not nome.strip():
            print("Nome do livro não pode ser vazio.")
            cursor.close()
            conn.close()
            return

        cursor.execute("SELECT * FROM livros WHERE titulo = %s", (nome,))
        livro_existente = cursor.fetchone()
        
        if livro_existente:
            cursor.execute("DELETE FROM livros WHERE titulo = %s", (nome,))
            conn.commit()
            print("Livro deletado com sucesso.")
        else:
            print("Livro não encontrado.")
        
        cursor.close()
        conn.close()
    else:
        print("Falha na conexão.")