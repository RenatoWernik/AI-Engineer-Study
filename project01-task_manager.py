lista_tarefas = []

while True:
    print("1 - Nova tarefa")
    print("2 - Ver tarefas")
    print("3 - Sair")
    print("4 - Excluir uma tarefa")
    print("5 - Editar tarefa")
    escolha = input("O que você deseja fazer? ")

    if escolha == "3":
        print("Até logo")
        break
    elif escolha == "2":
        if not lista_tarefas:
            print("Sua lista de tarefas esta vazia")
        else:
            for tarefa in lista_tarefas:
                print(tarefa)
    elif escolha == "1":
        nova_tarefa = input("Digite a tarefa que quer adicionar ")
        lista_tarefas.append(nova_tarefa)
        print("Lista de tarefas atualizadas: ",", ".join(lista_tarefas))

    elif escolha == "4":
        tarefa_to_remove = input("Digite o nome da tarefa que quer excluir ")
        if tarefa_to_remove not in lista_tarefas:
            print("Essa tarefa não existe")
        else:
            lista_tarefas.remove(tarefa_to_remove)
            print(f"A tarefa {tarefa_to_remove} foi removida.\n")
            print("Lista atual: ",", ".join(lista_tarefas))
    elif escolha == "5":
        tarefa_to_edit = input("Qual tarefa deseja editar? ")
        if tarefa_to_edit not in lista_tarefas:
            print("Essa tarefa não existe na lista de tarefas")
        else:
            tarefa_editada = input("Digite sua edição para a tarefa selecionada ")
            index_tarefa = lista_tarefas.index(tarefa_to_edit)
            lista_tarefas[index_tarefa] = tarefa_editada
            print("Lista atualizada: " , ", ".join(lista_tarefas))

    else:
        print("Opção inválida.")



