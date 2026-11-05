
from classes.resumo import Resumo
from banco.conexao import conectar


def listarResumos(id_estudante):
    conexao = conectar()

    if conexao is None:
        return []

    cursor = conexao.cursor()

    try:
        cursor.execute("""
            SELECT r.id_resumo, r.titulo_resumo,
                   r.conteudo, r.id_disciplina
            FROM resumo r
            INNER JOIN disciplina d
                ON r.id_disciplina = d.id_disciplina
            WHERE d.id_estudante = :id_estudante
            ORDER BY r.id_resumo
        """, {"id_estudante": id_estudante})

        resultados = cursor.fetchall()
        resumos = []

        for resultado in resultados:
            resumo = Resumo(
                resultado[0],
                resultado[1],
                resultado[2],
                resultado[3]
            )

            resumos.append(resumo)

        return resumos

    except Exception as erro:
        print("Erro ao listar resumos:", erro)
        return []

    finally:
        cursor.close()
        conexao.close()


def adicionarResumo(titulo, conteudo, id_disciplina, id_estudante):
    conexao = conectar()

    if conexao is None:
        return False

    cursor = conexao.cursor()

    try:
        cursor.execute("""
            INSERT INTO resumo (
                titulo_resumo,
                conteudo,
                id_disciplina
            )
            SELECT :titulo, :conteudo, id_disciplina
            FROM disciplina
            WHERE id_disciplina = :id_disciplina
            AND id_estudante = :id_estudante
        """, {
            "titulo": titulo,
            "conteudo": conteudo,
            "id_disciplina": id_disciplina,
            "id_estudante": id_estudante
        })

        if cursor.rowcount > 0:
            conexao.commit()
            return True

        conexao.rollback()
        return False

    except Exception as erro:
        print("Erro ao adicionar resumo:", erro)
        conexao.rollback()
        return False

    finally:
        cursor.close()
        conexao.close()


def editarResumo(id_resumo, titulo, conteudo,
                 id_disciplina, id_estudante):

    conexao = conectar()

    if conexao is None:
        return False

    cursor = conexao.cursor()

    try:
        cursor.execute("""
            UPDATE resumo
            SET titulo_resumo = :titulo,
                conteudo = :conteudo,
                id_disciplina = :id_disciplina
            WHERE id_resumo = :id_resumo
            AND EXISTS (
                SELECT 1
                FROM disciplina d
                WHERE d.id_disciplina = resumo.id_disciplina
                AND d.id_estudante = :id_estudante
            )
            AND EXISTS (
                SELECT 1
                FROM disciplina d
                WHERE d.id_disciplina = :id_disciplina
                AND d.id_estudante = :id_estudante
            )
        """, {
            "titulo": titulo,
            "conteudo": conteudo,
            "id_disciplina": id_disciplina,
            "id_resumo": id_resumo,
            "id_estudante": id_estudante
        })

        if cursor.rowcount > 0:
            conexao.commit()
            return True

        conexao.rollback()
        return False

    except Exception as erro:
        print("Erro ao editar resumo:", erro)
        conexao.rollback()
        return False

    finally:
        cursor.close()
        conexao.close()


def excluirResumo(id_resumo, id_estudante):
    conexao = conectar()

    if conexao is None:
        return False

    cursor = conexao.cursor()

    try:
        # Exclui os flashcards vinculados ao resumo
        cursor.execute("""
            DELETE FROM flashcard
            WHERE id_resumo = :id_resumo
            AND id_disciplina IN (
                SELECT id_disciplina
                FROM disciplina
                WHERE id_estudante = :id_estudante
            )
        """, {
            "id_resumo": id_resumo,
            "id_estudante": id_estudante
        })

        # Exclui o resumo
        cursor.execute("""
            DELETE FROM resumo
            WHERE id_resumo = :id_resumo
            AND id_disciplina IN (
                SELECT id_disciplina
                FROM disciplina
                WHERE id_estudante = :id_estudante
            )
        """, {
            "id_resumo": id_resumo,
            "id_estudante": id_estudante
        })

        if cursor.rowcount > 0:
            conexao.commit()
            return True

        conexao.rollback()
        return False

    except Exception as erro:
        print("Erro ao excluir resumo:", erro)
        conexao.rollback()
        return False

    finally:
        cursor.close()
        conexao.close()
