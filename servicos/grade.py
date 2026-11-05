
from banco.conexao import conectar


def obterIdGrade(id_estudante):
    conexao = conectar()

    if conexao is None:
        return None

    cursor = conexao.cursor()

    try:
        cursor.execute("""
            SELECT id_grade
            FROM grade
            WHERE id_estudante = :id_estudante
        """, {"id_estudante": id_estudante})

        resultado = cursor.fetchone()

        if resultado:
            return resultado[0]

        cursor.execute("""
            INSERT INTO grade (id_estudante)
            VALUES (:id_estudante)
        """, {"id_estudante": id_estudante})

        conexao.commit()

        cursor.execute("""
            SELECT id_grade
            FROM grade
            WHERE id_estudante = :id_estudante
        """, {"id_estudante": id_estudante})

        resultado = cursor.fetchone()

        if resultado:
            return resultado[0]

        return None

    except Exception as erro:
        print("Erro ao obter grade:", erro)
        conexao.rollback()
        return None

    finally:
        cursor.close()
        conexao.close()


def listarGrade(id_estudante):
    gradeAtual = [[""] * 5 for _ in range(5)]

    id_grade = obterIdGrade(id_estudante)

    if id_grade is None:
        return gradeAtual

    conexao = conectar()

    if conexao is None:
        return gradeAtual

    cursor = conexao.cursor()

    try:
        cursor.execute("""
            SELECT dia, horario, atividade
            FROM horarioGrade
            WHERE id_grade = :id_grade
        """, {"id_grade": id_grade})

        resultados = cursor.fetchall()

        dias = [
            "segunda-feira",
            "terça-feira",
            "quarta-feira",
            "quinta-feira",
            "sexta-feira"
        ]
        
        for resultado in resultados:
            dia = dias.index(resultado[0].lower())
            horario = resultado[1] - 1

            gradeAtual[horario][dia] = resultado[2]

        return gradeAtual

    except Exception as erro:
        print("Erro ao listar grade:", erro)
        return gradeAtual

    finally:
        cursor.close()
        conexao.close()


def salvarGrade(id_estudante, horarios):
    id_grade = obterIdGrade(id_estudante)

    if id_grade is None:
        return False

    conexao = conectar()

    if conexao is None:
        return False

    cursor = conexao.cursor()

    dias = [
        "segunda-feira",
        "terça-feira",
        "quarta-feira",
        "quinta-feira",
        "sexta-feira"
    ]

    try:
        cursor.execute("""
            DELETE FROM horarioGrade
            WHERE id_grade = :id_grade
        """, {"id_grade": id_grade})

        for horario in range(5):
            for dia in range(5):

                atividade = horarios[horario][dia]

                if atividade:
                    cursor.execute("""
                        INSERT INTO horarioGrade
                        (id_grade, dia, horario, atividade)
                        VALUES (:id_grade, :dia, :horario, :atividade)
                    """, {
                        "id_grade": id_grade,
                        "dia": dias[dia],
                        "horario": horario + 1,
                        "atividade": atividade
                    })

        conexao.commit()
        return True

    except Exception as erro:
        print("Erro ao salvar grade:", erro)
        conexao.rollback()
        return False

    finally:
        cursor.close()
        conexao.close()
