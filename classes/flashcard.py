class Flashcard:

    def __init__(self, id_flashcard, pergunta, resposta,
                 id_disciplina, id_resumo=None):

        self.id_flashcard = id_flashcard
        self.pergunta = pergunta
        self.resposta = resposta
        self.id_disciplina = id_disciplina
        self.id_resumo = id_resumo

    def editar(self, pergunta=None, resposta=None,
               id_disciplina=None, id_resumo=None):

        if pergunta:
            self.pergunta = pergunta

        if resposta:
            self.resposta = resposta

        if id_disciplina:
            self.id_disciplina = id_disciplina

        if id_resumo is not None:
            self.id_resumo = id_resumo