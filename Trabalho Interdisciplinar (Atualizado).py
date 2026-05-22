# lista principal - onde é armazenado cada tarefa
tarefas = []

# fluxo principal - onde é lido e coordenado a ação do menu
def main():
   while True:
        entrada = int(input("Input: "))
        if entrada == 1:
            adicionarTarefa()
        elif entrada == 2 :
            listarMenu()
        elif entrada == 3 :
            statusMenu()
        elif entrada == 4 :
           editarTarefa()
        elif entrada == 5 :
           excluirTarefa()
        elif entrada == 0 :
            print("Saindo...")
            break
        else:
            print("Opção Invalida!")

# função do menu - apenas mostra o menu e automaticamente executa o fluxo principal (main)
def menu():
    print("----------------- |Menu| -----------------")
    print('\n')
    print("1 = Adicionar Tarefa")
    print("2 = Listar Tarefas")
    print("3 = Marcar como concluido")
    print("4 = Editar Tarefa")
    print("5 = Excluir Tarefa")
    print("0 = Sair")
    print('\n')
    print("------------------------------------------")
    
    main()

# função de adicionar tarefa - toda criação da tarefa reside aqui, onde ele registra a tarefa e manda para lista principal (tarefas)
def adicionarTarefa():
    tarefa = []
    
    print("----------- |Adicionar Tarefa| -----------")
    print('\n')

    tarefa = {
        "nome": input('Nome da Tarefa: '),
        "descricao": input('Descrição: '),
        "disciplina": input('Disciplina: '),
        "prioridade": input("Prioridade (Baixa, Media e Alta): "),
        "status": "Pendente"
        }
    tarefas.append(tarefa)
    print('\n')
    print('Tarefa salva com sucesso!')
    print('\n')

    print("------------------------------------------")

    menu()

# função de listar tarefas - mostra e filtra cada tarefa criada por disciplina ou prioridade. mostra todas as informações delas e seu respectivo ID.
def listarMenu() :

   
   
    print("------------ |Listar Tarefas| ------------")
    print('\n')
    print("1 = Mostrar todas as tarefas")
    print("2 = Filtrar por disciplina")
    print("3 = Filtrar por prioridade")
    print('\n')
    print('\n')

    
    filtro = int(input("Escolha uma opção: "))
    
    # mostra todas as tarefas
    if filtro == 1 :
       if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
       else :
        for i, tarefa in enumerate(tarefas):
         print(f'\nID: {i}')
         print(f'Nome: {tarefa['nome']}')
         print(f'Descrição: {tarefa['descricao']}')
         print(f'Disciplina: {tarefa['disciplina']}')
         print(f'Prioridade: {tarefa['prioridade']}')
         print(f'Status: {tarefa['status']}')

    # filtra por disciplina 
    if filtro == 2 :
       if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
       else :
          disc = input("Informe a Disciplina: ")

          filtradas = [(i, t) for i, t in enumerate(tarefas) if t['disciplina'].lower() == disc.lower()]

          if not filtradas:
            print("Nenhuma tarefa encontrada.")
          else:
            for i, tarefa in filtradas:
               print(f'\nID: {i}')
               print(f'Nome: {tarefa["nome"]}')
               print(f'Descrição: {tarefa["descricao"]}')
               print(f'Disciplina: {tarefa["disciplina"]}')
               print(f'Prioridade: {tarefa["prioridade"]}')
               print(f'Status: {tarefa["status"]}')
    
    # filtra por prioridade
    if filtro == 3 :
       if not tarefas:
          print("Nenhuma tarefa cadastrada.")
          return
       else :
          prior = input("Informe a Prioridade: ")

          filtradas = [(i, t) for i, t in enumerate(tarefas) if t['prioridade'].lower() == prior.lower()]

          if not filtradas:
            print("Nenhuma tarefa encontrada.")
          else:
            for i, tarefa in filtradas:
               print(f'\nID: {i}')
               print(f'Nome: {tarefa["nome"]}')
               print(f'Descrição: {tarefa["descricao"]}')
               print(f'Disciplina: {tarefa["disciplina"]}')
               print(f'Prioridade: {tarefa["prioridade"]}')
               print(f'Status: {tarefa["status"]}')
                   
    print("------------------------------------------")
    menu()

# função de marcar como concluida - altera o status de uma tarefa (pendente/concluido)
def statusMenu() :
    print("------------ |Marcar Status| ------------")
    print('\n')
    
    if not tarefas :
       print("Nnehuma tarefa encontrada.")
       return
    else:
       for i, tarefa in enumerate(tarefas):
         print(f'\nID: {i}')
         print(f'Nome: {tarefa['nome']}')
         print(f'Status: {tarefa['status']}')

       print('\n')
       indice = int(input('Informe o ID da tarefa: '))
       if indice < 0 or indice >= len(tarefas):
            print("ID Inválido!")
            return
       else :
            print("1 = Concluída")
            print("2 = Pendente")
            print('\n')
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1 :
                  tarefas[indice]['status'] = "Concluída"
            elif opcao == 2 :
                  tarefas[indice]['status'] = "Pendente"
            else :
                  print("Opção Inválida!")
                  return

            print("Status atualizado com sucesso.") 
    print('\n')
    print("------------------------------------------")
    menu()

# função de editar tarefas - altera qualquer um dos valores da tarefa como nome, descrição e etc...
def editarTarefa() :
    print("---------------- |Editar| ----------------")
    print('\n')

    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    else :
        for i, tarefa in enumerate(tarefas):
         print(f'\nID: {i}')
         print(f'Nome: {tarefa['nome']}')
         print(f'Descrição: {tarefa['descricao']}')
         print(f'Disciplina: {tarefa['disciplina']}')
         print(f'Prioridade: {tarefa['prioridade']}')
         print(f'Status: {tarefa['status']}')

        print('\n')
        indice = int(input("Informe o ID da Tarefa: "))
        if indice < 0 or indice >= len(tarefas):
            print("ID Inválido!")
            return
        else :
            print("1 = Nome")
            print("2 = Descrição")
            print("3 = Disciplina")
            print("4 = Prioridade")
            print('\n')

            # altera somente a opção escolhida pelo usuario 
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1 :
               novoNome = input("Informe o novo nome: ")
               tarefas[indice]['nome'] = novoNome
            elif opcao == 2 :
               novaDesc = input("Informe a nova descrição: ")
               tarefas[indice]['descricao'] = novaDesc
            elif opcao == 3 :
               novaDisc = input("Informe a nova disciplina: ")
               tarefas[indice]['disciplina'] = novaDisc
            elif opcao == 4 :
               novaPrior = input("Informe a nova prioridade (Baixa, Media e Alta): ")
               tarefas[indice]['prioridade'] = novaPrior
    print('\n')
    print("Tarefa editada com sucesso.")
    print('\n')
    print("------------------------------------------")
    
    menu()

# função de excluir tarefas - apaga a tarefa selecionada no sistema. 
def excluirTarefa() :
   print("---------------- |Excluir| ----------------")
   print('\n')
   if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
   else :
        for i, tarefa in enumerate(tarefas):
         print(f'\nID: {i}')
         print(f'Nome: {tarefa['nome']}')
         print(f'Descrição: {tarefa['descricao']}')
         print(f'Disciplina: {tarefa['disciplina']}')
         print(f'Prioridade: {tarefa['prioridade']}')
         print(f'Status: {tarefa['status']}')
         print('\n')

        indice = int(input("Informe o ID da Tarefa: "))
        if indice < 0 or indice >= len(tarefas):
            print("ID Inválido!")
            return
        else :
           confirmacao = input("Deseja excluir a tarefa? (S/N): ").lower()

           if confirmacao == "s" or confirmacao == "sim":
                tarefas.pop(indice)
                print("Tarefa excluída com sucesso!")
           else:
                print("Exclusão cancelada.")
   print('\n')
   print("------------------------------------------")
   menu()

# inicio real do codigo
menu()