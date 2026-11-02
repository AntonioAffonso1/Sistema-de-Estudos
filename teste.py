
from classes.estudante import Estudante
from classes.tarefa import Tarefa


# Criando dois estudantes
estudante1 = Estudante("João", "joao@email.com", "123")
estudante2 = Estudante("Maria", "maria@email.com", "456")


# Criando tarefas
tarefa1 = Tarefa(
    "Estudar Python",
    "Revisar classes",
    "Programação",
    "Alta"
)

tarefa2 = Tarefa(
    "Estudar Matemática",
    "Resolver exercícios",
    "Matemática",
    "Média"
)


# Adicionando tarefas aos estudantes
estudante1.tarefas.append(tarefa1)
estudante2.tarefas.append(tarefa2)


# Adicionando atividades às grades
estudante1.grade.adicionarHorario(0, 0, "Python")
estudante2.grade.adicionarHorario(0, 0, "Matemática")


# Exibindo informações
print("----- ESTUDANTE 1 -----")
print(estudante1.nome)
print(estudante1.tarefas[0].nome)
print(estudante1.grade.visualizarGrade())

print("\n----- ESTUDANTE 2 -----")
print(estudante2.nome)
print(estudante2.tarefas[0].nome)
print(estudante2.grade.visualizarGrade())
