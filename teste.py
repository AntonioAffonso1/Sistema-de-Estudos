
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


from classes.resumo import Resumo

resumo1 = Resumo(
    1,
    "Introdução à Biologia",
    "Estudo das células e dos seres vivos.",
    2
)

print(resumo1.titulo)
print(resumo1.conteudo)

resumo1.editar(titulo="Biologia Celular")

print(resumo1.titulo)

from classes.flashcard import Flashcard

flashcard1 = Flashcard(
    1,
    "O que é fotossíntese?",
    "Processo pelo qual as plantas produzem seu alimento.",
    2
)

print(flashcard1.pergunta)
print(flashcard1.resposta)

flashcard1.editar(
    pergunta="Como funciona a fotossíntese?"
)

print(flashcard1.pergunta)

from classes.estudante import Estudante
from classes.resumo import Resumo
from classes.flashcard import Flashcard

estudante1 = Estudante("João", "joao@email.com", "123")
estudante2 = Estudante("Maria", "maria@email.com", "456")

resumo1 = Resumo(
    1, "Matemática", "Estudo de equações.", 1
)

flashcard1 = Flashcard(
    1, "O que é uma equação?", "Uma igualdade matemática.", 1
)

estudante1.resumos.append(resumo1)
estudante1.flashcards.append(flashcard1)

print("Resumos de João:", len(estudante1.resumos))
print("Resumos de Maria:", len(estudante2.resumos))

print("Flashcards de João:", len(estudante1.flashcards))
print("Flashcards de Maria:", len(estudante2.flashcards))