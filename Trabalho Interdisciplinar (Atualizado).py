# Lista contendo todos os usuarios cadastrados
usuarios = []

usuarioLogado = None

# Define a classe Usuario
class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

        # Nova mudança - Cada usuario tem suas tarefas separadas
        self.tarefas = []

        # Introdução da Grade de Estudos
        self.grade = [
            ["", "", "", "", ""],
            ["", "", "", "", ""],
            ["", "", "", "", ""],
            ["", "", "", "", ""],
            ["", "", "", "", ""]
        ]

# Define a classe Tarefa - Anteriormente usada apenas como variavel base
class Tarefa:

    def __init__(self, nome, descricao, disciplina, prioridade):

        self.nome = nome
        self.descricao = descricao
        self.disciplina = disciplina
        self.prioridade = prioridade
        self.status = "Pendente"

    def concluir(self):
        self.status = "Concluída"

    def editar(self, nome=None, descricao=None,
               disciplina=None, prioridade=None):

        if nome:
            self.nome = nome

        if descricao:
            self.descricao = descricao

        if disciplina:
            self.disciplina = disciplina

        if prioridade:
            self.prioridade = prioridade


# fluxo principal - onde é lido e coordenado a ação do menu
def main():
   while True:
        global usuarioLogado

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
        elif entrada == 6 :
           estatisticas()
        elif entrada == 7 :
            gradeEstudos()
        elif entrada == 0 :
            print("\nSaindo...\n")
            usuarioLogado = None
            telaInicial()
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
    print("6 = Exibir Estatisticas")
    print("7 = Grade de Estudos")
    print("0 = Sair")
    print('\n')
    print("------------------------------------------")
    
    main()

# função de adicionar tarefa - toda criação da tarefa reside aqui, onde ele registra a tarefa e manda para lista principal (tarefas)
def adicionarTarefa():
    
    print("----------- |Adicionar Tarefa| -----------")
    print('\n')

    novaTarefa = Tarefa(

        input("Nome da tarefa: "),
        input("Descrição: "),
        input("Disciplina: "),
        input("Prioridade: ")

    )

    usuarioLogado.tarefas.append(novaTarefa)
    
    print('\n')
    print('Tarefa salva com sucesso!')
    print('\n')

    print("------------------------------------------")

    menu()

# função de listar tarefas - mostra e filtra cada tarefa criada por disciplina ou prioridade. mostra todas as informações delas e seu respectivo ID.
def listarMenu():

   
   
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
       if not usuarioLogado.tarefas:
        print("Nenhuma tarefa cadastrada.")
        return menu()
       else :
        for i, Tarefa in enumerate(usuarioLogado.tarefas):
         print(f'\nID: {i}')
         print(f'Nome: {Tarefa.nome}')
         print(f'Descrição: {Tarefa.descricao}')
         print(f'Disciplina: {Tarefa.disciplina}')
         print(f'Prioridade: {Tarefa.prioridade}')
         print(f'Status: {Tarefa.status}')
         print('\n')

    # filtra por disciplina 
    if filtro == 2 :
       if not usuarioLogado.tarefas:
        print("Nenhuma tarefa cadastrada.")
        return menu()
       else :
          disc = input("Informe a Disciplina: ")

          filtradas = [(i, t) for i, t in enumerate(usuarioLogado.tarefas) if t.disciplina.lower() == disc.lower()]

          if not filtradas:
            print("Nenhuma tarefa encontrada.")
          else:
            for i, Tarefa in filtradas:
               print(f'\nID: {i}')
               print(f'Nome: {Tarefa.nome}')
               print(f'Descrição: {Tarefa.descricao}')
               print(f'Disciplina: {Tarefa.disciplina}')
               print(f'Prioridade: {Tarefa.prioridade}')
               print(f'Status: {Tarefa.status}')
               print('\n')
    
    # filtra por prioridade
    if filtro == 3 :
       if not usuarioLogado.tarefas:
          print("Nenhuma tarefa cadastrada.")
          return menu()
       else :
          prior = input("Informe a Prioridade: ")

          filtradas = [(i, t) for i, t in enumerate(usuarioLogado.tarefas) if t.prioridade.lower() == prior.lower()]

          if not filtradas:
            print("Nenhuma tarefa encontrada.")
          else:
            for i, Tarefa in filtradas:
               print(f'\nID: {i}')
               print(f'Nome: {Tarefa.nome}')
               print(f'Descrição: {Tarefa.descricao}')
               print(f'Disciplina: {Tarefa.disciplina}')
               print(f'Prioridade: {Tarefa.prioridade}')
               print(f'Status: {Tarefa.status}')
               print('\n')
                   
    print("------------------------------------------")
    menu()

# função de marcar como concluida - altera o status de uma tarefa (pendente/concluido)
def statusMenu():
    print("------------ |Marcar Status| ------------")
    print('\n')
    
    if not usuarioLogado.tarefas :
       print("Nnehuma tarefa encontrada.")
       return menu()
    else:
       for i, Tarefa in enumerate(usuarioLogado.tarefas):
         print(f'\nID: {i}')
         print(f'Nome: {Tarefa.nome}')
         print(f'Status: {Tarefa.status}')

       print('\n')
       indice = int(input('Informe o ID da tarefa: '))
       if indice < 0 or indice >= len(usuarioLogado.tarefas):
            print("ID Inválido!")
            return
       else :
            print("1 = Concluída")
            print("2 = Pendente")
            print('\n')
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1 :
                  usuarioLogado.tarefas[indice].status = "Concluída"
            elif opcao == 2 :
                  usuarioLogado.tarefas[indice].status = "Pendente"
            else :
                  print("Opção Inválida!")
                  return

            print("Status atualizado com sucesso.") 
    print('\n')
    print("------------------------------------------")
    menu()

# função de editar tarefas - altera qualquer um dos valores da tarefa como nome, descrição e etc...
def editarTarefa():
    print("---------------- |Editar| ----------------")
    print('\n')

    if not usuarioLogado.tarefas:
        print("Nenhuma tarefa cadastrada.")
        return menu()
    else :
        for i, Tarefa in enumerate(usuarioLogado.tarefas):
            print(f'\nID: {i}')
            print(f'Nome: {Tarefa.nome}')
            print(f'Descrição: {Tarefa.descricao}')
            print(f'Disciplina: {Tarefa.disciplina}')
            print(f'Prioridade: {Tarefa.prioridade}')
            print(f'Status: {Tarefa.status}')
            print('\n')

        print('\n')
        indice = int(input("Informe o ID da Tarefa: "))
        if indice < 0 or indice >= len(usuarioLogado.tarefas):
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
               usuarioLogado.tarefas[indice].nome = novoNome
            elif opcao == 2 :
               novaDesc = input("Informe a nova descrição: ")
               usuarioLogado.tarefas[indice].descricao = novaDesc
            elif opcao == 3 :
               novaDisc = input("Informe a nova disciplina: ")
               usuarioLogado.tarefas[indice].disciplina = novaDisc
            elif opcao == 4 :
               novaPrior = input("Informe a nova prioridade (Baixa, Media e Alta): ")
               usuarioLogado.tarefas[indice].prioridade = novaPrior
    print('\n')
    print("Tarefa editada com sucesso.")
    print('\n')
    print("------------------------------------------")
    
    menu()

# função de excluir tarefas - apaga a tarefa selecionada no sistema. 
def excluirTarefa():
   print("---------------- |Excluir| ----------------")
   print('\n')
   if not usuarioLogado.tarefas:
        print("Nenhuma tarefa cadastrada.")
        return menu()
   else :
        for i, Tarefa in enumerate(usuarioLogado.tarefas):
            print(f'\nID: {i}')
            print(f'Nome: {Tarefa.nome}')
            print(f'Descrição: {Tarefa.descricao}')
            print(f'Disciplina: {Tarefa.disciplina}')
            print(f'Prioridade: {Tarefa.prioridade}')
            print(f'Status: {Tarefa.status}')
            print('\n')

        indice = int(input("Informe o ID da Tarefa: "))
        if indice < 0 or indice >= len(usuarioLogado.tarefas):
            print("ID Inválido!")
            return
        else :
           confirmacao = input("Deseja excluir a tarefa? (S/N): ").lower()

           if confirmacao == "s" or confirmacao == "sim":
                usuarioLogado.tarefas.pop(indice)
                print("Tarefa excluída com sucesso!")
           else:
                print("Exclusão cancelada.")
   print('\n')
   print("------------------------------------------")
   menu()

# função exibir estatisticas - para mostrar o resumo/estatisticas das tarefas
def estatisticas():
    print("-------------- |Estatísticas| --------------")
    print()

    if not usuarioLogado.tarefas:
        print("Nenhuma tarefa cadastrada.")
        return menu()

    concluidas = 0
    pendentes = 0
    disciplinas = {}

    # Percorre todas as tarefas
    for Tarefa in usuarioLogado.tarefas:

        # Conta o status
        if Tarefa.status == "Concluída":
            concluidas += 1
        else:
            pendentes += 1

        # Conta as disciplinas
        disciplina = Tarefa.disciplina

        if disciplina in disciplinas:
            disciplinas[disciplina] += 1
        else:
            disciplinas[disciplina] = 1

    # Exibe o resumo
    print(f"Total de tarefas: {len(usuarioLogado.tarefas)}")
    print(f"Tarefas concluídas: {concluidas}")
    print(f"Tarefas pendentes: {pendentes}")

    print("\nQuantidade por disciplina:")
    for disciplina, quantidade in disciplinas.items():
        print(f"{disciplina}: {quantidade}")

    print()
    print("--------------------------------------------")
    menu()

def gradeEstudos():
    print("a")

def cadastroUsuario():
    print("---------------- |Cadastro| ----------------")
    print('\n')

    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")

    # verifica email repetido
    for usuario in usuarios:
        if usuario.email == email:
            print("Email já cadastrado.")
            return

    novoUsuario = Usuario(nome, email, senha)

    usuarios.append(novoUsuario)
    print("\nCadastro Realizado!")
    print('\n')
    print("--------------------------------------------")

    telaInicial()

def login():

    global usuarioLogado

    email = input("Email: ")
    senha = input("Senha: ")

    for usuario in usuarios:

        if usuario.email == email and usuario.senha == senha:

            usuarioLogado = usuario

            print(f"\nBem-vindo {usuario.nome}!\n")
            menu()
            return True

    print("Email ou senha incorretos.")

    return False

def telaInicial():

    print("---------------- |Inicio| ----------------")
    print('\n')
    print("1 = Login")
    print("2 = Cadastrar")
    print("0 = Sair")
    print('\n')
    print("------------------------------------------")

    entrada = int(input("Input: "))

    while True:
        if entrada == 1 :
            login()
        elif entrada == 2 :
            cadastroUsuario()
        elif entrada == 0 :
            print("Saindo...")
            break
        else :
            print("Opção Invalida!")
    

# inicio real do codigo - onde a função inicial é chamada e da inicio ao programa.
telaInicial()