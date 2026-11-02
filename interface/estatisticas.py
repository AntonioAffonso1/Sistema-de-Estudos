
import tkinter as tk

AZUL_PRINCIPAL = "#182c73"
AZUL_BOTOES = "#3d4c82"
FUNDO = "#f4f6fb"
BRANCO = "#ffffff"
TEXTO = "#202a44"


def telaEstatisticas(janela, estudante):

    # Limpa a tela anterior
    for componente in janela.winfo_children():
        componente.destroy()

    janela.configure(bg=FUNDO)

    # Cabeçalho
    cabecalho = tk.Frame(janela, bg=AZUL_PRINCIPAL, height=75)
    cabecalho.pack(fill="x")
    cabecalho.pack_propagate(False)

    titulo = tk.Label(
        cabecalho,
        text="Estatísticas",
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
    conteudo.pack(fill="both", expand=True, padx=30, pady=25)

    tk.Label(
        conteudo,
        text=f"Desempenho de {estudante.nome}",
        font=("Arial", 19, "bold"),
        bg=FUNDO,
        fg=TEXTO
    ).pack(anchor="w", pady=(0, 20))

    # Calcula as quantidades
        # Calcula as quantidades
    try:
        total = len(estudante.tarefas)
        concluidas = 0
        pendentes = 0

        disciplinas = {}

        for tarefa in estudante.tarefas:

            if tarefa.status == "Concluída":
                concluidas += 1
            else:
                pendentes += 1

            if tarefa.disciplina in disciplinas:
                disciplinas[tarefa.disciplina] += 1
            else:
                disciplinas[tarefa.disciplina] = 1

        if total > 0:
            percentual = (concluidas / total) * 100
        else:
            percentual = 0

    except Exception as erro:
        print("Erro ao calcular estatísticas:", erro)

        total = 0
        concluidas = 0
        pendentes = 0
        disciplinas = {}
        percentual = 0
        
    # Área dos indicadores
    indicadores = tk.Frame(conteudo, bg=FUNDO)
    indicadores.pack(fill="x", pady=10)

    def criarIndicador(pai, titulo, valor, cor):
        quadro = tk.Frame(
            pai,
            bg=BRANCO,
            padx=20,
            pady=20
        )

        tk.Label(
            quadro,
            text=titulo,
            font=("Arial", 11),
            bg=BRANCO,
            fg="#7b8499"
        ).pack()

        tk.Label(
            quadro,
            text=str(valor),
            font=("Arial", 25, "bold"),
            bg=BRANCO,
            fg=cor
        ).pack(pady=5)

        return quadro

    criarIndicador(
        indicadores, "Total de tarefas", total, AZUL_PRINCIPAL
    ).pack(side="left", fill="both", expand=True, padx=5)

    criarIndicador(
        indicadores, "Concluídas", concluidas, "#3b9875"
    ).pack(side="left", fill="both", expand=True, padx=5)

    criarIndicador(
        indicadores, "Pendentes", pendentes, "#cf5c66"
    ).pack(side="left", fill="both", expand=True, padx=5)

    # Percentual de conclusão
    quadroProgresso = tk.Frame(
        conteudo,
        bg=BRANCO,
        padx=20,
        pady=15
    )
    quadroProgresso.pack(fill="x", pady=15)

    tk.Label(
        quadroProgresso,
        text="Progresso das atividades",
        font=("Arial", 14, "bold"),
        bg=BRANCO,
        fg=AZUL_PRINCIPAL
    ).pack(anchor="w")

    tk.Label(
        quadroProgresso,
        text=f"{percentual:.1f}% das tarefas foram concluídas.",
        font=("Arial", 12),
        bg=BRANCO,
        fg=TEXTO
    ).pack(anchor="w", pady=8)

    # Barra de progresso
    barraFundo = tk.Frame(
        quadroProgresso,
        bg="#e5e9f2",
        height=18
    )
    barraFundo.pack(fill="x", pady=5)
    barraFundo.pack_propagate(False)

    barraProgresso = tk.Frame(
        barraFundo,
        bg="#3b9875",
        width=0,
        height=18
    )
    barraProgresso.place(
        relx=0,
        rely=0,
        relheight=1,
        relwidth=percentual / 100
    )

    # Distribuição por disciplina
    quadroDisciplinas = tk.Frame(
        conteudo,
        bg=BRANCO,
        padx=20,
        pady=15
    )
    quadroDisciplinas.pack(fill="both", expand=True, pady=10)

    tk.Label(
        quadroDisciplinas,
        text="Tarefas por disciplina",
        font=("Arial", 14, "bold"),
        bg=BRANCO,
        fg=AZUL_PRINCIPAL
    ).pack(anchor="w", pady=(0, 10))

    if disciplinas:
        for disciplina, quantidade in disciplinas.items():

            tk.Label(
                quadroDisciplinas,
                text=f"{disciplina}: {quantidade} tarefa(s)",
                font=("Arial", 11),
                bg=BRANCO,
                fg=TEXTO
            ).pack(anchor="w", pady=4)

    else:
        tk.Label(
            quadroDisciplinas,
            text="Nenhuma tarefa cadastrada.",
            font=("Arial", 11),
            bg=BRANCO,
            fg="#7b8499"
        ).pack(anchor="w")
