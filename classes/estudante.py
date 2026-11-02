#classe estudante

# importando a classe grade de estudos
from classes.grade_estudo import GradeEstudo

class Estudante:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

        self.tarefas = []
        self.resumos = []
        self.flashcards = []

        self.grade = GradeEstudo()