from classes.estudante import Estudante

estudantes = []


def cadastro(nome, email, senha):

    for estudante in estudantes:
        if estudante.email == email:
            return False

    novoEstudante = Estudante(nome, email, senha)
    estudantes.append(novoEstudante)

    return True


def login(email, senha):

    for estudante in estudantes:

        if estudante.email == email and estudante.senha == senha:
            return estudante

    return None