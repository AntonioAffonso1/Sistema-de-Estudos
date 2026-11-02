class Resumo:

    def __init__(self, id_resumo, titulo, conteudo, id_disciplina):
        self.id_resumo = id_resumo
        self.titulo = titulo
        self.conteudo = conteudo
        self.id_disciplina = id_disciplina

    def editar(self, titulo=None, conteudo=None, id_disciplina=None):

        if titulo:
            self.titulo = titulo

        if conteudo:
            self.conteudo = conteudo

        if id_disciplina:
            self.id_disciplina = id_disciplina