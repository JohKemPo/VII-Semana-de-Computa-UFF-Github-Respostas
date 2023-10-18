import gerenciador_de_contatos

while True:
    print("\nGerenciador de Contatos")
    print("1. Adicionar Contato")
    print("2. Listar Contatos")
    print("3. Buscar Contato")
    print("4. Deletar Contato")
    print("5. Sair")

    escolha = input("Informe sua escolha: ")

    if escolha == '1':
        nome = input("Informe o nome: ")
        telefone = input("Informe o telefone: ")
        gerenciador_de_contatos.adicionar_contato(nome, telefone)
        print("Contato adicionado.")

    elif escolha == '2':
        gerenciador_de_contatos.listar_contatos()

    elif escolha == '3':
        nome = input("Informe o nome para busca: ")
        contato = gerenciador_de_contatos.buscar_contato(nome)
        if contato:
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}")
        else:
            print("Contato não encontrado.")

    elif escolha == '4':
        nome = input("Informe o nome para deletar: ")
        gerenciador_de_contatos.deletar_contato(nome)

    elif escolha == '5':
        print("Até logo!")
        break

    else:
        print("Escolha inválida. Por favor, tente novamente.")
