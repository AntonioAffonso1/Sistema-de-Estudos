# Classe da grade de estudos

class GradeEstudo:

    def __init__(self):

        # Matriz de horários (5 horários x 5 dias)
        self.horarios = [
            ["", "", "", "", ""],
            ["", "", "", "", ""],
            ["", "", "", "", ""],
            ["", "", "", "", ""],
            ["", "", "", "", ""]
        ]

    # Adicionar atividade na grade
    def adicionarHorario(self, horario, dia, atividade):

        if 0 <= horario < 5 and 0 <= dia < 5:
            self.horarios[horario][dia] = atividade
            return True

        return False

    # Remover atividade da grade
    def removerHorario(self, horario, dia):

        if 0 <= horario < 5 and 0 <= dia < 5:
            self.horarios[horario][dia] = ""
            return True

        return False

    # Visualizar matriz
    def visualizarGrade(self):
        return self.horarios
