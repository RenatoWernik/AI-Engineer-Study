#Projeto: Task Manager 2.0 (com dicionários)
#O objetivo é reescrever o gestor de tarefas para que cada tarefa tenha um número único de identificação, um ID. O utilizador passa a escolher as tarefas pelo ID, não pelo nome.
#Isto mata de vez o fantasma da tarefa duplicada: mesmo que tenhas duas tarefas com o texto "estudar", cada uma tem o seu ID próprio e são distinguíveis.

#cada tarefa tem um ID unico
#user escolhe tarefas pelo ID,não pelo nome
#isso soluciona o problema de tarefas com nomes iguais
#chave é o ID
#texto da tarefa é o value

#Funcionalidades:
    #Add nova tarefa
    #Ver tarefas
    #Editar tarefa
    #Remover tarefa
    #Sair

#ainda vou adicionar edge cases (tarefas fora do dicionario,dicionario vazio,)
tasks = {}    
counter_id = 1
while True:
    



    print("O que deseja fazer? ")
    choice = input("1 - Add Nova Tarefa\n2 - Ver Tarefas\n3 - Editar Tarefa\n4 - Remover Tarefa\n5 - Sair\n")

    if choice == "1":
        new_task = input("Digite a tarefa a ser adicionada: ")
        tasks[counter_id] = new_task
        
        print(f"A tarefa foi adicionada: {counter_id} - {new_task.title()}")
        counter_id = counter_id + 1
        
    elif choice == "2":
        if not tasks:
            print("Sem tarefas no momento. ")
        else:
            for task_id,task_name in tasks.items():
                print(f"{task_id} - {task_name.title()}")
                
    
    elif choice == "3":
        print(tasks)
        task_to_edit = int(input("Qual tarefa você deseja editar? Responda com o ID da tarefa: "))
        if task_to_edit not in tasks:
            print("Essa tarefa não existe.")
        else:
            task_editing = input(f"Digite a nova descrição para a tarefa {task_to_edit}: ")
            tasks[task_to_edit] = task_editing
            for task_id,task_name in tasks.items():
                print(f"{task_id} - {task_name.title()}")
    elif choice == "4":
        for task_id,task_name in tasks.items():
                print(f"{task_id} - {task_name.title()}")
        task_to_remove = int(input("Qual tarefa deseja remover? Digite o ID da tarefa: "))
        if task_to_remove not in tasks:
            print("Essa tarefa não existe. ")
        else:
            del(tasks[task_to_remove])
            for task_id,task_name in tasks.items():
                print(f"Tarefa {task_to_remove} removida\n{task_id} - {task_name.title()}")
    elif choice == "5":
        break


#TODO: proteger contra input não numérico com try/except quando aprender exceções
