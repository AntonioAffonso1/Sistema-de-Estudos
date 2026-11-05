from banco.conexao import conectar

conexao = conectar()

if conexao:
    cursor = conexao.cursor()

    cursor.execute("SELECT nome FROM estudante")

    for resultado in cursor:
        print(resultado[0])

    cursor.close()
    conexao.close()