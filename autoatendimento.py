from config import conexao
from sistemaAutoatendimento import autenticacao, emprestar, livros


def main():
    conn = conexao.conectar()

    if not conn:
        print("Falha na conexão.")
        return

    print("Conexão bem-sucedida!")

    while True:
        print("\nMenu de Autoatendimento:")
        print("1. Cadastrar usuário")
        print("2. Login")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                autenticacao.cadastrar()

            case "2":
                usuario_id = autenticacao.login()

                if usuario_id:
                    while True:
                        print("\nMenu de Autoatendimento:")
                        print("1. Listar livros")
                        print("2. Listar empréstimos")
                        print("3. Emprestar livro")
                        print("4. Devolver livro")
                        print("0. Sair")

                        sub_opcao = input("Escolha uma opção: ")

                        match sub_opcao:
                            case "1":
                                livros.listar_livros()

                            case "2":
                                emprestar.listar_emprestimos(
                                    usuario_id
                                )

                            case "3":
                                emprestar.emprestar_livro(
                                    usuario_id
                                )

                            case "4":
                                emprestar.devolver_livro(
                                    usuario_id
                                )

                            case "0":
                                break

                            case _:
                                print("Opção inválida.")

                else:
                    print("Login inválido. Acesso negado.")

            case "0":
                print("Saindo do sistema.")
                break

            case _:
                print("Opção inválida.")

    conn.close()


if __name__ == "__main__":
    main()