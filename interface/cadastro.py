
import tkinter as tk

from servicos.autenticacao import cadastro


# Cores
AZUL_PRINCIPAL = "#182c73"
AZUL_SECUNDARIO = "#15255e"
AZUL_BOTOES = "#3d4c82"
FUNDO = "#f4f6fb"
BRANCO = "#ffffff"
TEXTO = "#202a44"


def telaCadastro(janela):

    # Preparação da tela
    for componente in janela.winfo_children():
        componente.destroy()

    janela.configure(bg=FUNDO)

    # Funções
    def realizarCadastro():
        nome = campoNome.get()
        email = campoEmail.get()
        senha = campoSenha.get()
        confirmarSenha = campoConfirmarSenha.get()

        if not nome or not email or not senha or not confirmarSenha:
            mensagem.config(
                text="Preencha todos os campos.",
                fg="#cf5c66"
            )
            return

        if senha != confirmarSenha:
            mensagem.config(
                text="As senhas não correspondem.",
                fg="#cf5c66"
            )
            return

        resultado = cadastro(nome, email, senha)

        if resultado:
            mensagem.config(
                text="Cadastro realizado com sucesso!",
                fg="#3b9875"
            )
        else:
            mensagem.config(
                text="Este e-mail já está cadastrado.",
                fg="#cf5c66"
            )

    def voltarLogin():
        from interface.login import telaLogin
        telaLogin(janela)

    # Quadro principal
    quadro = tk.Frame(
        janela,
        bg=BRANCO,
        padx=40,
        pady=35
    )
    quadro.place(relx=0.5, rely=0.5, anchor="center")

    titulo = tk.Label(
        quadro,
        text="Criar conta",
        font=("Arial", 22, "bold"),
        bg=BRANCO,
        fg=AZUL_PRINCIPAL
    )
    titulo.pack(pady=(0, 10))

    descricao = tk.Label(
        quadro,
        text="Preencha os dados para se cadastrar.",
        font=("Arial", 11),
        bg=BRANCO,
        fg="#7b8499"
    )
    descricao.pack(pady=(0, 20))

    # Campos de cadastro
    tk.Label(
        quadro,
        text="Nome completo",
        font=("Arial", 11),
        bg=BRANCO,
        fg=TEXTO
    ).pack(anchor="w")

    campoNome = tk.Entry(
        quadro,
        font=("Arial", 12),
        width=30
    )
    campoNome.pack(pady=(5, 12))

    tk.Label(
        quadro,
        text="E-mail",
        font=("Arial", 11),
        bg=BRANCO,
        fg=TEXTO
    ).pack(anchor="w")

    campoEmail = tk.Entry(
        quadro,
        font=("Arial", 12),
        width=30
    )
    campoEmail.pack(pady=(5, 12))

    tk.Label(
        quadro,
        text="Senha",
        font=("Arial", 11),
        bg=BRANCO,
        fg=TEXTO
    ).pack(anchor="w")

    campoSenha = tk.Entry(
        quadro,
        font=("Arial", 12),
        width=30,
        show="*"
    )
    campoSenha.pack(pady=(5, 12))

    tk.Label(
        quadro,
        text="Confirmar senha",
        font=("Arial", 11),
        bg=BRANCO,
        fg=TEXTO
    ).pack(anchor="w")

    campoConfirmarSenha = tk.Entry(
        quadro,
        font=("Arial", 12),
        width=30,
        show="*"
    )
    campoConfirmarSenha.pack(pady=(5, 12))

    # Mensagem
    mensagem = tk.Label(
        quadro,
        text="",
        font=("Arial", 10),
        bg=BRANCO,
        fg="#cf5c66"
    )
    mensagem.pack(pady=5)

    # Botões
    botaoCadastrar = tk.Button(
        quadro,
        text="Cadastrar",
        font=("Arial", 11, "bold"),
        bg=AZUL_BOTOES,
        fg=BRANCO,
        activebackground=AZUL_SECUNDARIO,
        activeforeground=BRANCO,
        width=25,
        cursor="hand2",
        command=realizarCadastro
    )
    botaoCadastrar.pack(pady=10)

    botaoVoltar = tk.Button(
        quadro,
        text="Voltar para Login",
        font=("Arial", 10),
        bg=BRANCO,
        fg=AZUL_PRINCIPAL,
        relief="flat",
        cursor="hand2",
        command=voltarLogin
    )
    botaoVoltar.pack()
