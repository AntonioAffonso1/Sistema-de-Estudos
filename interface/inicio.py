
import tkinter as tk

AZUL_PRINCIPAL = "#182c73"
AZUL_SECUNDARIO = "#15255e"
AZUL_BOTOES = "#3d4c82"
FUNDO = "#f4f6fb"
BRANCO = "#ffffff"
TEXTO = "#202a44"


def telaInicio(janela, estudante):

    # Limpa os componentes da tela anterior
    for componente in janela.winfo_children():
        componente.destroy()

    janela.configure(bg=FUNDO)

    # Cabeçalho
    cabecalho = tk.Frame(
        janela,
        bg=AZUL_PRINCIPAL,
        height=90
    )
    cabecalho.pack(fill="x")
    cabecalho.pack_propagate(False)

    titulo = tk.Label(
        cabecalho,
        text="Sistema de Estudos",
        font=("Arial", 22, "bold"),
        bg=AZUL_PRINCIPAL,
        fg=BRANCO
    )
    titulo.pack(side="left", padx=30, pady=25)

    def abrirTarefas():
        from interface.tarefas import telaTarefas
        telaTarefas(janela, estudante)

    def abrirGrade():
        from interface.grade import telaGrade
        telaGrade(janela, estudante)

    def sair():
        from interface.login import telaLogin
        telaLogin(janela)

    def abrirEstatisticas():
        from interface.estatisticas import telaEstatisticas
        telaEstatisticas(janela, estudante)

    def abrirDisciplinas():
        from interface.disciplinas import telaDisciplinas
        telaDisciplinas(janela, estudante)

    def abrirResumos():
        from interface.resumos import telaResumos
        telaResumos(janela, estudante)

    def abrirFlashcards():
        from interface.flashcards import telaFlashcards
        telaFlashcards(janela, estudante)

    botaoSair = tk.Button(
        cabecalho,
        text="Sair",
        font=("Arial", 10, "bold"),
        bg=AZUL_BOTOES,
        fg=BRANCO,
        relief="flat",
        cursor="hand2",
        command=sair
    )
    botaoSair.pack(side="right", padx=30, pady=25)

    # Conteúdo principal
    conteudo = tk.Frame(
        janela,
        bg=FUNDO
    )
    conteudo.pack(fill="both", expand=True, padx=35, pady=30)

    mensagem = tk.Label(
        conteudo,
        text=f"Bem-vindo(a), {estudante.nome}!",
        font=("Arial", 22, "bold"),
        bg=FUNDO,
        fg=TEXTO
    )
    mensagem.pack(anchor="w", pady=(0, 8))

    descricao = tk.Label(
        conteudo,
        text="Organize suas tarefas e sua rotina de estudos.",
        font=("Arial", 12),
        bg=FUNDO,
        fg="#7b8499"
    )
    descricao.pack(anchor="w", pady=(0, 30))

    # Área dos menus
    menus = tk.Frame(conteudo, bg=FUNDO)
    menus.pack(fill="x")

    # Botão de tarefas
    botaoTarefas = tk.Button(
        menus,
        text="Minhas tarefas",
        font=("Arial", 13, "bold"),
        bg=BRANCO,
        fg=AZUL_PRINCIPAL,
        width=25,
        height=4,
        relief="flat",
        cursor="hand2",
        command=abrirTarefas
    )
    botaoTarefas.grid(row=0, column=0, padx=10, pady=10)

    # Botão da grade
    botaoGrade = tk.Button(
        menus,
        text="Grade de estudos",
        font=("Arial", 13, "bold"),
        bg=BRANCO,
        fg=AZUL_PRINCIPAL,
        width=25,
        height=4,
        relief="flat",
        cursor="hand2",
        command=abrirGrade
    )
    botaoGrade.grid(row=0, column=1, padx=10, pady=10)

    # Botão de estatísticas
    botaoEstatisticas = tk.Button(
        menus,
        text="Estatísticas",
        font=("Arial", 13, "bold"),
        bg=BRANCO,
        fg=AZUL_PRINCIPAL,
        width=25,
        height=4,
        relief="flat",
        cursor="hand2",
        command=abrirEstatisticas
    )
    botaoEstatisticas.grid(row=1, column=0, padx=10, pady=10)

        # Botão de disciplinas
    botaoDisciplinas = tk.Button(
        menus,
        text="Minhas disciplinas",
        font=("Arial", 13, "bold"),
        bg=BRANCO,
        fg=AZUL_PRINCIPAL,
        width=25,
        height=4,
        relief="flat",
        cursor="hand2",
        command=abrirDisciplinas
    )
    botaoDisciplinas.grid(row=1, column=1, padx=10, pady=10)

        # Botão de resumos
    botaoResumos = tk.Button(
        menus,
        text="Meus resumos",
        font=("Arial", 13, "bold"),
        bg=BRANCO,
        fg=AZUL_PRINCIPAL,
        width=25,
        height=4,
        relief="flat",
        cursor="hand2",
        command=abrirResumos
    )
    botaoResumos.grid(row=2, column=0, padx=10, pady=10)

    botaoFlashcards = tk.Button(
        menus,
        text="Meus Flashcards",
        font=("Arial", 13, "bold"),
        bg=BRANCO,
        fg=AZUL_PRINCIPAL,
        width=25,
        height=4,
        relief="flat",
        cursor="hand2",
        command=abrirFlashcards
    )

    botaoFlashcards.grid(
        row=2,
        column=1,
        padx=10,
        pady=10
    )

