
from classes.estudante import Estudante

estudantes = []


def cadastro(nome, email, senha):
    try:
        for estudante in estudantes:
            if estudante.email == email:
                return False

        novoEstudante = Estudante(nome, email, senha)
        estudantes.append(novoEstudante)

        return True

    except Exception as erro:
        print("Erro ao realizar cadastro:", erro)
        return False


def login(email, senha):
    try:
        for estudante in estudantes:
            if estudante.email == email and estudante.senha == senha:
                return estudante

        return None

    except Exception as erro:
        print("Erro ao realizar login:", erro)
        return None
