import gerenciador_de_tarefas

while True:
    print("\nGerenciador de Tarefas")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Deletar Tarefa")
    print("5. Sair")

    escolha = input("Informe sua escolha: ")

    if escolha == '1':
        nome_tarefa = input("Informe o nome da tarefa: ")
        data_limite = input("Informe a data limite: ")
        gerenciador_de_tarefas.adicionar_tarefa(nome_tarefa, data_limite)
        print("Tarefa adicionada.")

    elif escolha == '2':
        gerenciador_de_tarefas.listar_tarefas()

    elif escolha == '3':
        gerenciador_de_tarefas.listar_tarefas()
        indice_tarefa = int(input("Informe o índice da tarefa a ser marcada como concluída: "))
        gerenciador_de_tarefas.marcar_tarefa_como_concluida(indice_tarefa)

    elif escolha == '4':
        gerenciador_de_tarefas.listar_tarefas()
        indice_tarefa = int(input("Informe o índice da tarefa a ser deletada: "))
        gerenciador_de_tarefas.deletar_tarefa(indice_tarefa)

    elif escolha == '5':
        print("Até logo!")
        break

    else:
        print("Escolha inválida. Por favor, tente novamente.")