from config import conexao
from sistemaBiblioteca import gerenciarUsuarios,gerenciarCategorias, gerenciarLivros, gerenciarEmprestimos


def main():
    conn = conexao.conectar()
    if conn:
        print("Conexão bem-sucedida!")
        conn.close()
    else:
        print("Falha na conexão.")

    while True:
        print("\nMenu:")
        print("1. Gerenciar usuários")
        print("2. Gerenciar categorias")
        print("3. Gerenciar livros")
        print("4. Gerenciar empréstimos")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                while True:
                    print("\nGerenciar Usuários:")
                    print("1. Adicionar usuário")
                    print("2. Listar usuários")
                    print("3. Atualizar usuário")
                    print("4. Deletar usuário")
                    print("0. Voltar ao menu principal")

                    sub_opcao = input("Escolha uma opção: ")

                    match sub_opcao:
                        case "1":
                            gerenciarUsuarios.adicionar_usuario()
                        case "2":
                            gerenciarUsuarios.listar_usuarios()
                        case "3":
                            gerenciarUsuarios.atualizar_usuario()
                        case "4":
                            gerenciarUsuarios.deletar_usuario()
                        case "0":
                            break
                        case _:
                            print("Opção inválida.")
            case "2":
                while True:
                    print("\nGerenciar Categorias:")
                    print("1. Adicionar categoria")
                    print("2. Listar categorias")
                    print("3. Atualizar categoria")
                    print("4. Deletar categoria")
                    print("0. Voltar ao menu principal")

                    sub_opcao = input("Escolha uma opção: ")

                    match sub_opcao:
                        case "1":
                            gerenciarCategorias.adicionar_categoria()
                        case "2":
                            gerenciarCategorias.listar_categorias()
                        case "3":
                            gerenciarCategorias.atualizar_categoria()
                        case "4":
                            gerenciarCategorias.deletar_categoria()
                        case "0":
                            break
                        case _:
                            print("Opção inválida.")
            case "3":
                while True:
                    print("\nGerenciar Livros:")
                    print("1. Adicionar livro")
                    print("2. Listar livros")
                    print("3. Atualizar livro")
                    print("4. Deletar livro")
                    print("0. Voltar ao menu principal")

                    sub_opcao = input("Escolha uma opção: ")

                    match sub_opcao:
                        case "1":
                            gerenciarLivros.adicionar_livro()
                        case "2":
                            gerenciarLivros.listar_livros()
                        case "3":
                            gerenciarLivros.atualizar_livro()
                        case "4":
                            gerenciarLivros.deletar_livro()
                        case "0":
                            break
                        case _:
                            print("Opção inválida.")
            case "4":
                while True:
                    print("\nGerenciar Empréstimos:")
                    print("1. Realizar empréstimo")
                    print("2. Listar empréstimos")
                    print("3. Devolver livro")
                    print("0. Voltar ao menu principal")

                    sub_opcao = input("Escolha uma opção: ")

                    match sub_opcao:
                        case "1":
                            gerenciarEmprestimos.realizar_emprestimo()
                        case "2":
                            gerenciarEmprestimos.listar_emprestimos()
                        case "3":
                            gerenciarEmprestimos.devolver_livro()
                        case "0":
                            break
                        case _:
                            print("Opção inválida.")
            
            case "0":
                print("Saindo do sistema...")
                break
            case _:
                print("Opção inválida.")

if __name__ == "__main__":
    main()