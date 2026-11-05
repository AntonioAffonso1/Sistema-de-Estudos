
from classes.flashcard import Flashcard
from banco.conexao import conectar


def listarFlashcards(id_estudante):
    conexao = conectar()

    if conexao is None:
        return []

    cursor = conexao.cursor()

    try:
        cursor.execute("""
            SELECT f.id_flashcard,
                   f.pergunta,
                   f.resposta,
                   f.id_disciplina,
                   f.id_resumo
            FROM flashcard f
            INNER JOIN disciplina d
                ON f.id_disciplina = d.id_disciplina
            WHERE d.id_estudante = :id_estudante
            ORDER BY f.id_flashcard
        """, {"id_estudante": id_estudante})

        resultados = cursor.fetchall()
        flashcards = []

        for resultado in resultados:
            flashcard = Flashcard(
                resultado[0],
                resultado[1],
                resultado[2],
                resultado[3],
                resultado[4]
            )

            flashcards.append(flashcard)

        return flashcards

    except Exception as erro:
        print("Erro ao listar flashcards:", erro)
        return []

    finally:
        cursor.close()
        conexao.close()


def adicionarFlashcard(pergunta, resposta, id_disciplina,
                       id_resumo, id_estudante):

    conexao = conectar()

    if conexao is None:
        return False

    cursor = conexao.cursor()

    try:
        cursor.execute("""
            INSERT INTO flashcard (
                pergunta,
                resposta,
                id_disciplina,
                id_resumo
            )
            SELECT :pergunta,
                   :resposta,
                   d.id_disciplina,
                   :id_resumo
            FROM disciplina d
            WHERE d.id_disciplina = :id_disciplina
            AND d.id_estudante = :id_estudante
            AND (
                :id_resumo IS NULL
                OR EXISTS (
                    SELECT 1
                    FROM resumo r
                    WHERE r.id_resumo = :id_resumo
                    AND r.id_disciplina = d.id_disciplina
                )
            )
        """, {
            "pergunta": pergunta,
            "resposta": resposta,
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
        print("Erro ao adicionar flashcard:", erro)
        conexao.rollback()
        return False

    finally:
        cursor.close()
        conexao.close()


def editarFlashcard(id_flashcard, pergunta, resposta,
                    id_disciplina, id_resumo, id_estudante):

    conexao = conectar()

    if conexao is None:
        return False

    cursor = conexao.cursor()

    try:
        cursor.execute("""
            UPDATE flashcard f
            SET pergunta = :pergunta,
                resposta = :resposta,
                id_disciplina = :id_disciplina,
                id_resumo = :id_resumo
            WHERE f.id_flashcard = :id_flashcard
            AND EXISTS (
                SELECT 1
                FROM disciplina d
                WHERE d.id_disciplina = f.id_disciplina
                AND d.id_estudante = :id_estudante
            )
            AND EXISTS (
                SELECT 1
                FROM disciplina d
                WHERE d.id_disciplina = :id_disciplina
                AND d.id_estudante = :id_estudante
                AND (
                    :id_resumo IS NULL
                    OR EXISTS (
                        SELECT 1
                        FROM resumo r
                        WHERE r.id_resumo = :id_resumo
                        AND r.id_disciplina = d.id_disciplina
                    )
                )
            )
        """, {
            "pergunta": pergunta,
            "resposta": resposta,
            "id_disciplina": id_disciplina,
            "id_resumo": id_resumo,
            "id_flashcard": id_flashcard,
            "id_estudante": id_estudante
        })

        if cursor.rowcount > 0:
            conexao.commit()
            return True

        conexao.rollback()
        return False

    except Exception as erro:
        print("Erro ao editar flashcard:", erro)
        conexao.rollback()
        return False

    finally:
        cursor.close()
        conexao.close()


def excluirFlashcard(id_flashcard, id_estudante):
    conexao = conectar()

    if conexao is None:
        return False

    cursor = conexao.cursor()

    try:
        cursor.execute("""
            DELETE FROM flashcard
            WHERE id_flashcard = :id_flashcard
            AND id_disciplina IN (
                SELECT id_disciplina
                FROM disciplina
                WHERE id_estudante = :id_estudante
            )
        """, {
            "id_flashcard": id_flashcard,
            "id_estudante": id_estudante
        })

        if cursor.rowcount > 0:
            conexao.commit()
            return True

        conexao.rollback()
        return False

    except Exception as erro:
        print("Erro ao excluir flashcard:", erro)
        conexao.rollback()
        return False

    finally:
        cursor.close()
        conexao.close()
