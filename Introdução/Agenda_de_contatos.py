contatos = []

def adicionar_contato(nome, telefone):
    contato = {'nome': nome, 'telefone': telefone}
    contatos.append(contato)

def listar_contatos():
    for contato in contatos:
        print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}")

def buscar_contato(nome):
    for contato in contatos:
        if contato['nome'] == nome:
            return contato
    return None

def deletar_contato(nome):
    contato = buscar_contato(nome)
    if contato:
        contatos.remove(contato)
        print(f"Contato {nome} deletado.")
    else:
        print(f"Contato {nome} não encontrado.")

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
        adicionar_contato(nome, telefone)
        print("Contato adicionado.")

    elif escolha == '2':
        listar_contatos()

    elif escolha == '3':
        nome = input("Informe o nome para busca: ")
        contato = buscar_contato(nome)
        if contato:
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}")
        else:
            print("Contato não encontrado.")

    elif escolha == '4':
        nome = input("Informe o nome para deletar: ")
        deletar_contato(nome)

    elif escolha == '5':
        print("Até logo!")
        break

    else:
        print("Escolha inválida. Por favor, tente novamente.")
