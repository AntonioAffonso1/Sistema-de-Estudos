class Disciplina:

    def __init__(self, id, nome, descricao):
        self.id = id
        self.nome = nome
        self.descricao = descricao

    def editar(self, nome=None, descricao=None):

        if nome:
            self.nome = nome

        if descricao:
            self.descricao = descricao