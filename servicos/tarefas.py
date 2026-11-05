
from classes.tarefa import Tarefa
from banco.conexao import conectar


def listarTarefas(id_estudante):
    conexao = conectar()

    if conexao is None:
        return []

    cursor = conexao.cursor()

    try:
        cursor.execute("""
            SELECT
                t.id_tarefa,
                t.titulo_tarefa,
                t.descricao,
                d.nome,
                t.prioridade,
                TO_CHAR(t.data_prazo, 'DD/MM/YYYY'),
                t.status,
                t.id_disciplina
            FROM tarefa t
            INNER JOIN disciplina d
                ON t.id_disciplina = d.id_disciplina
            WHERE d.id_estudante = :id_estudante
            ORDER BY t.id_tarefa
        """, {"id_estudante": id_estudante})

        resultados = cursor.fetchall()
        tarefas = []

        for resultado in resultados:
            tarefa = Tarefa(
                resultado[1],
                resultado[2],
                resultado[3],
                resultado[4],
                resultado[5]
            )

            tarefa.id_tarefa = resultado[0]
            tarefa.status = resultado[6]
            tarefa.id_disciplina = resultado[7]

            tarefas.append(tarefa)

        return tarefas

    except Exception as erro:
        print("Erro ao listar tarefas:", erro)
        return []

    finally:
        cursor.close()
        conexao.close()


def adicionarTarefa(nome, descricao, id_disciplina,
                    prioridade, prazo, id_estudante):

    conexao = conectar()

    if conexao is None:
        return False

    cursor = conexao.cursor()

    try:
        cursor.execute("""
            INSERT INTO tarefa
            (titulo_tarefa, descricao, id_disciplina,
             prioridade, data_prazo, status)
            SELECT
                :nome, :descricao, id_disciplina,
                :prioridade,
                TO_DATE(:prazo, 'DD/MM/YYYY'),
                'Pendente'
            FROM disciplina
            WHERE id_disciplina = :id_disciplina
            AND id_estudante = :id_estudante
        """, {
            "nome": nome,
            "descricao": descricao,
            "id_disciplina": id_disciplina,
            "prioridade": prioridade,
            "prazo": prazo,
            "id_estudante": id_estudante
        })

        if cursor.rowcount == 0:
            return False

        conexao.commit()
        return True

    except Exception as erro:
        print("Erro ao adicionar tarefa:", erro)
        conexao.rollback()
        return False

    finally:
        cursor.close()
        conexao.close()


def editarTarefa(id_tarefa, nome, descricao,
                 id_disciplina, prioridade, prazo, id_estudante):

    conexao = conectar()

    if conexao is None:
        return False

    cursor = conexao.cursor()

    try:
        cursor.execute("""
            UPDATE tarefa
            SET titulo_tarefa = :nome,
                descricao = :descricao,
                id_disciplina = :id_disciplina,
                prioridade = :prioridade,
                data_prazo = TO_DATE(:prazo, 'DD/MM/YYYY')
            WHERE id_tarefa = :id_tarefa
            AND EXISTS (
                SELECT 1
                FROM disciplina d
                WHERE d.id_disciplina = tarefa.id_disciplina
                AND d.id_estudante = :id_estudante
            )
            AND EXISTS (
                SELECT 1
                FROM disciplina d
                WHERE d.id_disciplina = :id_disciplina
                AND d.id_estudante = :id_estudante
            )
        """, {
            "nome": nome,
            "descricao": descricao,
            "id_disciplina": id_disciplina,
            "prioridade": prioridade,
            "prazo": prazo,
            "id_tarefa": id_tarefa,
            "id_estudante": id_estudante
        })

        conexao.commit()
        return cursor.rowcount > 0

    except Exception as erro:
        print("Erro ao editar tarefa:", erro)
        conexao.rollback()
        return False

    finally:
        cursor.close()
        conexao.close()


def concluirTarefa(id_tarefa, id_estudante):

    conexao = conectar()

    if conexao is None:
        return False

    cursor = conexao.cursor()

    try:
        cursor.execute("""
            UPDATE tarefa
            SET status = 'Concluída'
            WHERE id_tarefa = :id_tarefa
            AND EXISTS (
                SELECT 1
                FROM disciplina d
                WHERE d.id_disciplina = tarefa.id_disciplina
                AND d.id_estudante = :id_estudante
            )
        """, {
            "id_tarefa": id_tarefa,
            "id_estudante": id_estudante
        })

        conexao.commit()
        return cursor.rowcount > 0

    except Exception as erro:
        print("Erro ao concluir tarefa:", erro)
        conexao.rollback()
        return False

    finally:
        cursor.close()
        conexao.close()


def excluirTarefa(id_tarefa, id_estudante):

    conexao = conectar()

    if conexao is None:
        return False

    cursor = conexao.cursor()

    try:
        cursor.execute("""
            DELETE FROM tarefa
            WHERE id_tarefa = :id_tarefa
            AND EXISTS (
                SELECT 1
                FROM disciplina d
                WHERE d.id_disciplina = tarefa.id_disciplina
                AND d.id_estudante = :id_estudante
            )
        """, {
            "id_tarefa": id_tarefa,
            "id_estudante": id_estudante
        })

        conexao.commit()
        return cursor.rowcount > 0

    except Exception as erro:
        print("Erro ao excluir tarefa:", erro)
        conexao.rollback()
        return False

    finally:
        cursor.close()
        conexao.close()
