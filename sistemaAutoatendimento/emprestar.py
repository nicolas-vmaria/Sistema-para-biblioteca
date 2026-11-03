from config import conexao
import datetime

def listar_emprestimos(usuario_id):
    conn = conexao.conectar()
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT l.titulo, e.data_emprestimo, e.data_devolucao FROM emprestimos e "
            "JOIN livros l ON e.livro_id = l.id WHERE e.usuario_id = %s",
            (usuario_id,),
        )
        emprestimos = cursor.fetchall()
        if not emprestimos:
            print("Nenhum empréstimo encontrado.")
        else:
            for emprestimo in emprestimos:
                print(
                    f"Livro: {emprestimo[0]}, Data de Empréstimo: {emprestimo[1]}, Data de Devolução: {emprestimo[2]}"
                )
        cursor.close()
        conn.close()
    else:
        print("Falha na conexão.")
        
        
def emprestar_livro(usuario_id):
    conn = conexao.conectar()
    if conn:
        cursor = conn.cursor()
        try:
            nomeLivro = input("Digite o nome do livro que deseja emprestar: ")

            if not nomeLivro.strip():
                print("O nome do livro não pode estar vazio.")
                return

            cursor.execute("SELECT id, titulo FROM livros WHERE titulo = %s", (nomeLivro,))
            livro = cursor.fetchone()

            if not livro:
                print("Livro não encontrado.")
                return

            cursor.execute(
                "UPDATE livros SET quantidade = quantidade - 1 "
                "WHERE id = %s AND quantidade > 0",
                (livro[0],),
            )
            if cursor.rowcount == 0:
                print("Não há cópias disponíveis deste livro.")
                return

            cursor.execute(
                "INSERT INTO emprestimos "
                "(data_emprestimo, data_devolucao, usuario_id, livro_id) "
                "VALUES (%s, %s, %s, %s)",
                (
                    datetime.date.today(),
                    datetime.date.today() + datetime.timedelta(days=7),
                    usuario_id,
                    livro[0],
                ),
            )
            conn.commit()
            print("Livro emprestado com sucesso.")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Falha na conexão.")
        

def devolver_livro(usuario_id):
    conn = conexao.conectar()
    if conn:
        cursor = conn.cursor()
        try:
            nomeLivro = input("Digite o nome do livro que deseja devolver: ")

            if not nomeLivro.strip():
                print("O nome do livro não pode estar vazio.")
                return

            cursor.execute("SELECT id FROM livros WHERE titulo = %s", (nomeLivro,))
            livro = cursor.fetchone()

            if not livro:
                print("Livro não encontrado.")
                return

            cursor.execute(
                "SELECT id FROM emprestimos WHERE usuario_id = %s AND livro_id = %s",
                (usuario_id, livro[0]),
            )
            emprestimo = cursor.fetchone()

            if not emprestimo:
                print("Nenhum empréstimo encontrado para este livro.")
                return

            cursor.execute("DELETE FROM emprestimos WHERE id = %s", (emprestimo[0],))
            cursor.execute(
                "UPDATE livros SET quantidade = quantidade + 1 WHERE id = %s",
                (livro[0],),
            )
            conn.commit()
            print("Livro devolvido com sucesso.")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Falha na conexão.")