# classe tarefa


class Tarefa:
    def __init__(self, nome, descricao, disciplina, prioridade, prazo):
        self.nome = nome
        self.descricao = descricao
        self.disciplina = disciplina
        self.prioridade = prioridade
        self.prazo = prazo
        self.status = "Pendente"

    def concluir(self):
        self.status = "Concluída"

    def editar(self, nome=None, descricao=None,
               disciplina=None, prioridade=None, prazo=None):

        if nome:
            self.nome = nome
        if descricao:
            self.descricao = descricao
        if disciplina:
            self.disciplina = disciplina
        if prioridade:
            self.prioridade = prioridade
        if prazo:
            self.prazo = prazo
