contatos = []

def adicionar_contato(nome, telefone):
    contato = {'nome': nome, 'telefone': telefone}
    contatos.append(contato)

def listar_contatos():
    for contato in contatos:
        print(f"\nNome: {contato['nome']}, Telefone: {contato['telefone']}")

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
