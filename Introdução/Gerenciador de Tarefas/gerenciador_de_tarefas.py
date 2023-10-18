
tarefas = []

def adicionar_tarefa(nome_tarefa, data_limite):
    tarefa = {'nome_tarefa': nome_tarefa, 'data_limite': data_limite, 'completada': False}
    tarefas.append(tarefa)

def listar_tarefas():
    print("Lista de Tarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "Concluída" if tarefa['completada'] else "Não Concluída"
        print(f"\n{i}. {tarefa['nome_tarefa']} (Data Limite: {tarefa['data_limite']}, Status: {status})")

def marcar_tarefa_como_concluida(indice_tarefa):
    if 1 <= indice_tarefa <= len(tarefas):
        tarefa = tarefas[indice_tarefa - 1]
        tarefa['completada'] = True
        print(f"Tarefa '{tarefa['nome_tarefa']}' marcada como concluída.")
    else:
        print("Índice de tarefa inválido.")

def deletar_tarefa(indice_tarefa):
    if 1 <= indice_tarefa <= len(tarefas):
        tarefa_deletada = tarefas.pop(indice_tarefa - 1)
        print(f"Tarefa '{tarefa_deletada['nome_tarefa']}' deletada.")
    else:
        print("Índice de tarefa inválido.")