
from classes.disciplina import Disciplina
from banco.conexao import conectar


def listarDisciplinas(id_estudante):
    conexao = conectar()

    if conexao is None:
        return []

    cursor = conexao.cursor()

    try:
        cursor.execute("""
            SELECT id_disciplina, nome, desc_disciplina
            FROM disciplina
            WHERE id_estudante = :id_estudante
            ORDER BY id_disciplina
        """, {"id_estudante": id_estudante})

        resultados = cursor.fetchall()
        disciplinas = []

        for resultado in resultados:
            disciplina = Disciplina(
                resultado[0],
                resultado[1],
                resultado[2]
            )

            disciplinas.append(disciplina)

        return disciplinas

    except Exception as erro:
        print("Erro ao listar disciplinas:", erro)
        return []

    finally:
        cursor.close()
        conexao.close()


def adicionarDisciplina(nome, descricao, id_estudante):
    conexao = conectar()

    if conexao is None:
        return False

    cursor = conexao.cursor()

    try:
        cursor.execute("""
            INSERT INTO disciplina
            (nome, desc_disciplina, id_estudante)
            VALUES (:nome, :descricao, :id_estudante)
        """, {
            "nome": nome,
            "descricao": descricao,
            "id_estudante": id_estudante
        })

        conexao.commit()
        return True

    except Exception as erro:
        print("Erro ao adicionar disciplina:", erro)
        conexao.rollback()
        return False

    finally:
        cursor.close()
        conexao.close()


def editarDisciplina(id_disciplina, nome, descricao, id_estudante):
    conexao = conectar()

    if conexao is None:
        return False

    cursor = conexao.cursor()

    try:
        cursor.execute("""
            UPDATE disciplina
            SET nome = :nome,
                desc_disciplina = :descricao
            WHERE id_disciplina = :id_disciplina
            AND id_estudante = :id_estudante
        """, {
            "nome": nome,
            "descricao": descricao,
            "id_disciplina": id_disciplina,
            "id_estudante": id_estudante
        })

        conexao.commit()
        return cursor.rowcount > 0

    except Exception as erro:
        print("Erro ao editar disciplina:", erro)
        conexao.rollback()
        return False

    finally:
        cursor.close()
        conexao.close()


def excluirDisciplina(id_disciplina, id_estudante):
    conexao = conectar()

    if conexao is None:
        return False

    cursor = conexao.cursor()

    try:
        cursor.execute("""
            DELETE FROM disciplina
            WHERE id_disciplina = :id_disciplina
            AND id_estudante = :id_estudante
        """, {
            "id_disciplina": id_disciplina,
            "id_estudante": id_estudante
        })

        conexao.commit()
        return cursor.rowcount > 0

    except Exception as erro:
        print("Erro ao excluir disciplina:", erro)
        conexao.rollback()
        return False

    finally:
        cursor.close()
        conexao.close()
