
import tkinter as tk

from servicos.autenticacao import login


# Cores
AZUL_PRINCIPAL = "#182c73"
AZUL_SECUNDARIO = "#15255e"
AZUL_BOTOES = "#3d4c82"
FUNDO = "#f4f6fb"
BRANCO = "#ffffff"
TEXTO = "#202a44"


def telaLogin(janela):

    # Preparação da tela
    for componente in janela.winfo_children():
        componente.destroy()

    janela.configure(bg=FUNDO)

    # Funções
    def abrirCadastro():
        from interface.cadastro import telaCadastro
        telaCadastro(janela)

    def verificarLogin():

        email = campoEmail.get()
        senha = campoSenha.get()

        if not email or not senha:
            mensagem.config(text="Preencha todos os campos.")
            return

        estudante = login(email, senha)

        if estudante is not None:
            from interface.inicio import telaInicio
            telaInicio(janela, estudante)
        else:
            mensagem.config(text="E-mail ou senha incorretos.")

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
        text="Sistema de Estudos",
        font=("Arial", 22, "bold"),
        bg=BRANCO,
        fg=AZUL_PRINCIPAL
    )
    titulo.pack(pady=(0, 10))

    descricao = tk.Label(
        quadro,
        text="Entre com sua conta",
        font=("Arial", 11),
        bg=BRANCO,
        fg=TEXTO
    )
    descricao.pack(pady=(0, 25))

    # Campos de login
    tk.Label(
        quadro,
        text="E-mail",
        bg=BRANCO,
        fg=TEXTO,
        font=("Arial", 10)
    ).pack(anchor="w")

    campoEmail = tk.Entry(
        quadro,
        font=("Arial", 12),
        width=30
    )
    campoEmail.pack(pady=(5, 15))

    tk.Label(
        quadro,
        text="Senha",
        bg=BRANCO,
        fg=TEXTO,
        font=("Arial", 10)
    ).pack(anchor="w")

    campoSenha = tk.Entry(
        quadro,
        font=("Arial", 12),
        width=30,
        show="*"
    )
    campoSenha.pack(pady=(5, 20))

    # Mensagem
    mensagem = tk.Label(
        quadro,
        text="",
        bg=BRANCO,
        fg="#cf5c66",
        font=("Arial", 9)
    )
    mensagem.pack()

    # Botões
    botaoLogin = tk.Button(
        quadro,
        text="Entrar",
        font=("Arial", 11, "bold"),
        bg=AZUL_BOTOES,
        fg=BRANCO,
        activebackground=AZUL_SECUNDARIO,
        activeforeground=BRANCO,
        width=25,
        relief="flat",
        command=verificarLogin
    )
    botaoLogin.pack(pady=15)

    botaoCadastro = tk.Button(
        quadro,
        text="Criar uma conta",
        font=("Arial", 10),
        bg=BRANCO,
        fg=AZUL_PRINCIPAL,
        relief="flat",
        cursor="hand2",
        command=abrirCadastro
    )
    botaoCadastro.pack()
