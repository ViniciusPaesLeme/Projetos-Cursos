# Lista vazia para armazenar os livros e variável para controle de IDs
lista_livros = []
id_global = 0

cadastroDeLivro = "Menu Cadastrar Livro"
princMenu = "Menu principal"
consulMenu = "Menu Consultar Livro"


# Função para cadastrar um livro
def cadastrar_livro():
    global id_global
    id_global += 1
    
    print(cadastroDeLivro.center(60, '-'))
    print('id do livro ', id_global)
    nome = input("Entre com o nome do livro: ")
    autor = input("Entre com o nome do autor: ")
    editora = input("Entre com o nome da editora: ")
    
    print('*' * 60)
    
    livro = {"id": id_global, "nome": nome, "autor": autor, "editora": editora}
    lista_livros.append(livro)
    print("Livro cadastrado com sucesso!")

# Função para consultar livros
def consultar_livro():
    
    print(consulMenu.center(60, '-'))
    
    opcao = input("Qual opção deseja?\n1. Consultar Todos\n2. Consultar por Id\n3. Consultar por Autor\n4. Retornar ao menu\n>> ")
    
    if opcao == '1': # Consultar Todos
        if lista_livros:
            for livro in lista_livros:
                print("id:", livro["id"])
                print("nome:", livro["nome"])
                print("autor:", livro["autor"])
                print("editora:", livro["editora"])
                print('-' * 30)
        else:
            print("Não há livros cadastrados.")
    elif opcao == '2': # Consultar por Id
        id_consulta = int(input("Entre com o id do livro: "))
        for livro in lista_livros:
            if livro['id'] == id_consulta:
                print("id:", livro["id"])
                print("nome:", livro["nome"])
                print("autor:", livro["autor"])
                print("editora:", livro["editora"])
                break
        else:
            print("Livro não encontrado.")
    elif opcao == '3': # Consultar por Autor
        autor_consulta = input("Entre com o nome do autor: ")
        encontrados = False
        for livro in lista_livros:
            if livro['autor'] == autor_consulta:
                print("id:", livro["id"])
                print("nome:", livro["nome"])
                print("autor:", livro["autor"])
                print("editora:", livro["editora"])
                encontrados = True
        if not encontrados:
            print("Não há livros cadastrados deste autor.")
    elif opcao == '4': # Retornar ao menu
        return
    else:
        print("Opção inválida.")

# Função para remover um livro
def remover_livro():
    id_remover = int(input("Entre com o id do livro a ser removido: "))
    for livro in lista_livros:
        if livro['id'] == id_remover:
            lista_livros.remove(livro)
            print("Livro removido com sucesso!")
            return
    else:
        print("Livro não encontrado.")

# Função principal
def main():
    while True:
        print(princMenu.center(60, '-'))
        print("Menu:")
        print("1. Cadastrar Livro")
        print("2. Consultar Livro")
        print("3. Remover Livro")
        print("4. Encerrar Programa")
        
        opcao_menu = input("Escolha uma opção: \n>>")
        
        print('*' * 60)
        
        if opcao_menu == '1': # Cadastrar Livro
            cadastrar_livro()
            print("Operação concluída.")
        elif opcao_menu == '2': # Consultar Livro
            consultar_livro()
        elif opcao_menu == '3': # Remover Livro
            remover_livro()
        elif opcao_menu == '4': # Encerrar Programa
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida.")
            
# Mensagem de boas-vindas
print("Bem-vindo ao software de gerenciamento de livros!")
print('*' * 60)

if __name__ == "__main__":
    main()
