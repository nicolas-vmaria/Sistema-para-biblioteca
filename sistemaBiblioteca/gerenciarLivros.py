from config import conexao
from mysql.connector import IntegrityError


def _ler_quantidade(valor):
    try:
        quantidade = int(valor)
    except ValueError:
        return None
    return quantidade if 0 <= quantidade <= 2_147_483_647 else None

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
        quantidade = _ler_quantidade(quantidade)
        if quantidade is None:
            print("Quantidade deve ser um número inteiro maior ou igual a zero.")
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
            cursor.execute("INSERT INTO livros (titulo, autor, categoria_id, quantidade) "
                           "VALUES (%s, %s, %s, %s)",
                           (nome, autor, categoria_existente[0], quantidade))
            conn.commit()
            print("Livro adicionado com sucesso.")
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

        cursor.execute(
            "SELECT id, titulo, autor, categoria_id, quantidade "
            "FROM livros WHERE titulo = %s",
            (nome_antigo,),
        )
        livro_existente = cursor.fetchone()
        
        if livro_existente:
            titulo_digitado = input(
                "Digite o novo nome do livro (vazio para manter): "
            ).strip()
            autor_digitado = input(
                "Digite o novo autor do livro (vazio para manter): "
            ).strip()
            categoria_digitada = input(
                "Digite a nova categoria do livro (vazio para manter): "
            ).strip()
            quantidade_digitada = input(
                "Digite a nova quantidade (vazio para manter): "
            ).strip()

            titulo_novo = (
                titulo_digitado.capitalize() if titulo_digitado else livro_existente[1]
            )
            autor_novo = (
                autor_digitado.title() if autor_digitado else livro_existente[2]
            )
            categoria_id = livro_existente[3]
            quantidade_nova = livro_existente[4]

            if categoria_digitada:
                cursor.execute(
                    "SELECT id FROM categorias WHERE nome = %s",
                    (categoria_digitada.capitalize(),),
                )
                categoria_existente = cursor.fetchone()

                if not categoria_existente:
                    print("Categoria não encontrada.")
                    cursor.close()
                    conn.close()
                    return

                categoria_id = categoria_existente[0]

            if quantidade_digitada:
                quantidade_validada = _ler_quantidade(quantidade_digitada)
                if quantidade_validada is None:
                    print(
                        "Quantidade deve ser um número inteiro maior ou igual a zero."
                    )
                    cursor.close()
                    conn.close()
                    return

                quantidade_nova = quantidade_validada

            cursor.execute(
                "UPDATE livros SET titulo = %s, autor = %s, categoria_id = %s, "
                "quantidade = %s WHERE titulo = %s",
                (titulo_novo, autor_novo, categoria_id, quantidade_nova, nome_antigo),
            )
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
            try:
                cursor.execute("DELETE FROM livros WHERE titulo = %s", (nome,))
                conn.commit()
                print("Livro deletado com sucesso.")
            except IntegrityError:
                conn.rollback()
                print("Não é possível excluir o livro porque há empréstimos associados.")
        else:
            print("Livro não encontrado.")
        
        cursor.close()
        conn.close()
    else:
        print("Falha na conexão.")