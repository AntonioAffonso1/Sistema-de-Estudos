import oracledb

def conectar():
    try:
        conexao = oracledb.connect(
            user="ADMAPPTAREFAS",
            password="admapp1234",
            dsn="localhost:1521/XEPDB1"
        )


        return conexao

    except Exception as erro:
        print("Erro ao conectar com Oracle:", erro)
        return None