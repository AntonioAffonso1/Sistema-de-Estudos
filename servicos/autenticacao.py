
from classes.estudante import Estudante
from banco.conexao import conectar


def cadastro(nome, email, senha):
    conexao = conectar()

    if conexao is None:
        return False

    cursor = conexao.cursor()

    try:
        cursor.execute("""
            INSERT INTO estudante (nome, email, senha)
            VALUES (:nome, :email, :senha)
        """, {
            "nome": nome,
            "email": email,
            "senha": senha
        })

        conexao.commit()
        return True

    except Exception as erro:
        print("Erro ao realizar cadastro:", erro)
        conexao.rollback()
        return False

    finally:
        cursor.close()
        conexao.close()


def login(email, senha):
    conexao = conectar()

    if conexao is None:
        return None

    cursor = conexao.cursor()

    try:
        cursor.execute("""
            SELECT id_estudante, nome, email, senha
            FROM estudante
            WHERE email = :email AND senha = :senha
        """, {
            "email": email,
            "senha": senha
        })

        resultado = cursor.fetchone()

        if resultado:
            estudante = Estudante(
                resultado[1],
                resultado[2],
                resultado[3],
                resultado[0]
            )

            return estudante

        return None

    except Exception as erro:
        print("Erro ao realizar login:", erro)
        return None

    finally:
        cursor.close()
        conexao.close()
