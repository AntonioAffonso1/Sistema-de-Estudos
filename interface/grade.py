
import tkinter as tk
from servicos.grade import listarGrade, salvarGrade as salvarGradeBanco

AZUL_PRINCIPAL = "#182c73"
AZUL_SECUNDARIO = "#15255e"
AZUL_BOTOES = "#3d4c82"
FUNDO = "#f4f6fb"
BRANCO = "#ffffff"
TEXTO = "#202a44"

dias = [
    "Segunda",
    "Terça",
    "Quarta",
    "Quinta",
    "Sexta"
]

horarios = [
    "1ª Aula",
    "2ª Aula",
    "3ª Aula",
    "4ª Aula",
    "5ª Aula"
]


def telaGrade(janela, estudante):

    # Limpa a tela anterior
    for componente in janela.winfo_children():
        componente.destroy()

    janela.configure(bg=FUNDO)

    # Cabeçalho
    cabecalho = tk.Frame(
        janela,
        bg=AZUL_PRINCIPAL,
        height=75
    )
    cabecalho.pack(fill="x")
    cabecalho.pack_propagate(False)

    titulo = tk.Label(
        cabecalho,
        text="Grade de estudos",
        font=("Arial", 20, "bold"),
        bg=AZUL_PRINCIPAL,
        fg=BRANCO
    )
    titulo.pack(side="left", padx=30, pady=20)

    def voltar():
        from interface.inicio import telaInicio
        telaInicio(janela, estudante)

    botaoVoltar = tk.Button(
        cabecalho,
        text="Voltar",
        font=("Arial", 10, "bold"),
        bg=AZUL_BOTOES,
        fg=BRANCO,
        relief="flat",
        cursor="hand2",
        command=voltar
    )
    botaoVoltar.pack(side="right", padx=30, pady=20)

    # Conteúdo principal
    conteudo = tk.Frame(janela, bg=FUNDO)
    conteudo.pack(fill="both", expand=True, padx=25, pady=25)

    descricao = tk.Label(
        conteudo,
        text="Organize suas atividades durante a semana.",
        font=("Arial", 12),
        bg=FUNDO,
        fg="#7b8499"
    )
    descricao.pack(anchor="w", pady=(0, 20))

    # Área da grade
    quadroGrade = tk.Frame(
        conteudo,
        bg=BRANCO,
        padx=15,
        pady=15
    )
    quadroGrade.pack(fill="both", expand=True)

    # Matriz que armazenará os campos da interface
    campos = []

    # Cabeçalho dos dias
    tk.Label(
        quadroGrade,
        text="Horários",
        font=("Arial", 10, "bold"),
        bg=BRANCO,
        fg=AZUL_PRINCIPAL,
        width=12
    ).grid(row=0, column=0, padx=3, pady=8)

    for dia in range(5):
        tk.Label(
            quadroGrade,
            text=dias[dia],
            font=("Arial", 10, "bold"),
            bg=BRANCO,
            fg=AZUL_PRINCIPAL,
            width=17
        ).grid(row=0, column=dia + 1, padx=3, pady=8)

    # Criação das linhas e campos
    gradeAtual = listarGrade(estudante.id_estudante)

    for horario in range(5):

        linha = []

        tk.Label(
            quadroGrade,
            text=horarios[horario],
            font=("Arial", 10, "bold"),
            bg=BRANCO,
            fg=TEXTO,
            width=12
        ).grid(row=horario + 1, column=0, padx=3, pady=8)

        for dia in range(5):

            campo = tk.Entry(
                quadroGrade,
                font=("Arial", 10),
                width=17,
                justify="center"
            )

            campo.grid(
                row=horario + 1,
                column=dia + 1,
                padx=3,
                pady=8,
                ipady=8
            )

            # Recupera a atividade já cadastrada
            if gradeAtual[horario][dia]:
                campo.insert(0, gradeAtual[horario][dia])

            linha.append(campo)

        campos.append(linha)

    mensagem = tk.Label(
        conteudo,
        text="",
        font=("Arial", 10),
        bg=FUNDO,
        fg="#3b9875"
    )
    mensagem.pack(pady=10)

    # Salvar as alterações

    def salvarGrade():
        try:
            horariosAtualizados = [[""] * 5 for _ in range(5)]

            for horario in range(5):
                for dia in range(5):
                    horariosAtualizados[horario][dia] = campos[horario][dia].get()

            sucesso = salvarGradeBanco(
                estudante.id_estudante,
                horariosAtualizados
            )

            if sucesso:
                mensagem.config(
                    text="Grade salva com sucesso!",
                    fg="#3b9875"
                )
            else:
                mensagem.config(
                    text="Erro ao salvar a grade no banco de dados.",
                    fg="#cf5c66"
                )

        except Exception as erro:
            print("Erro ao salvar grade:", erro)
            mensagem.config(
                text="Ocorreu um erro ao salvar a grade.",
                fg="#cf5c66"
            )

    botaoSalvar = tk.Button(
        conteudo,
        text="Salvar grade",
        font=("Arial", 11, "bold"),
        bg=AZUL_PRINCIPAL,
        fg=BRANCO,
        activebackground=AZUL_SECUNDARIO,
        activeforeground=BRANCO,
        relief="flat",
        cursor="hand2",
        width=20,
        command=salvarGrade
    )
    botaoSalvar.pack(pady=10)
