from config import conexao
import datetime

def realizar_emprestimo():
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

            nomeUsuario = input("Digite o nome do usuário que está realizando o empréstimo: ")
            if not nomeUsuario.strip():
                print("Nome do usuário não pode ser vazio.")
                return

            cursor.execute("SELECT id, nome FROM usuarios WHERE nome = %s", (nomeUsuario,))
            usuario = cursor.fetchone()
            if not usuario:
                print("Usuário não encontrado.")
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
                "INSERT INTO emprestimos (data_emprestimo, data_devolucao, usuario_id, livro_id) "
                "VALUES (%s, %s, %s, %s)",
                (
                    datetime.date.today(),
                    datetime.date.today() + datetime.timedelta(days=7),
                    usuario[0],
                    livro[0],
                ),
            )
            conn.commit()
            print(f"Empréstimo realizado com sucesso! {usuario[1]} emprestou {livro[1]}.")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Falha na conexão.")
        
        
def listar_emprestimos():
    conn = conexao.conectar()
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT u.nome, l.titulo, e.data_emprestimo, e.data_devolucao FROM emprestimos e "
            "JOIN usuarios u ON e.usuario_id = u.id "
            "JOIN livros l ON e.livro_id = l.id"
        )
        emprestimos = cursor.fetchall()
        
        if not emprestimos:
            print("Nenhum empréstimo encontrado.")
        else:
            print("\nLista de Empréstimos:")
            for emprestimo in emprestimos:
                print(f"Usuário: {emprestimo[0]}, Livro: {emprestimo[1]}, Data de Empréstimo: {emprestimo[2]}, Data de Devolução: {emprestimo[3]}")
        cursor.close()
        conn.close()
    else:
        print("Falha na conexão.")
        

def devolver_livro():
    conn = conexao.conectar()
    if conn:
        cursor = conn.cursor()
        try:
            nomeLivro = input("Digite o nome do livro que deseja devolver: ")

            if not nomeLivro.strip():
                print("O nome do livro não pode estar vazio.")
                return

            cursor.execute("SELECT id, titulo FROM livros WHERE titulo = %s", (nomeLivro,))
            livro = cursor.fetchone()

            if not livro:
                print("Livro não encontrado.")
                return

            nomeUsuario = input("Digite o nome do usuário que está devolvendo o livro: ")
            if not nomeUsuario.strip():
                print("Nome do usuário não pode ser vazio.")
                return

            cursor.execute("SELECT id, nome FROM usuarios WHERE nome = %s", (nomeUsuario,))
            usuario = cursor.fetchone()
            if not usuario:
                print("Usuário não encontrado.")
                return

            cursor.execute(
                "SELECT id FROM emprestimos WHERE usuario_id = %s AND livro_id = %s LIMIT 1",
                (usuario[0], livro[0]),
            )
            emprestimo = cursor.fetchone()
            if not emprestimo:
                print("Empréstimo não encontrado.")
                return

            cursor.execute("DELETE FROM emprestimos WHERE id = %s", (emprestimo[0],))
            cursor.execute(
                "UPDATE livros SET quantidade = quantidade + 1 WHERE id = %s",
                (livro[0],),
            )
            conn.commit()
            print(f"Devolução realizada com sucesso! {usuario[1]} devolveu {livro[1]}.")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Falha na conexão.")