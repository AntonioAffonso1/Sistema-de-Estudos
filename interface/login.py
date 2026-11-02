
import tkinter as tk

from servicos.autenticacao import login


AZUL_PRINCIPAL = "#182c73"
AZUL_SECUNDARIO = "#15255e"
AZUL_BOTOES = "#3d4c82"

FUNDO = "#f4f6fb"
BRANCO = "#ffffff"
TEXTO = "#202a44"


def telaLogin(janela):

    # Limpar conteúdo anterior da janela
    for componente in janela.winfo_children():
        componente.destroy()

    janela.configure(bg=FUNDO)

    # Área central
    quadro = tk.Frame(
        janela,
        bg=BRANCO,
        padx=40,
        pady=35
    )
    quadro.place(relx=0.5, rely=0.5, anchor="center")

    # Título
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

    # Campo de e-mail
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

    # Campo de senha
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

    # Mensagem de retorno
    mensagem = tk.Label(
        quadro,
        text="",
        bg=BRANCO,
        fg="#cf5c66",
        font=("Arial", 9)
    )
    mensagem.pack()

    # Função do botão
    def verificarLogin():

        email = campoEmail.get()
        senha = campoSenha.get()

        if not email or not senha:
            mensagem.config(text="Preencha todos os campos.")
            return

        estudante = login(email, senha)

        if estudante is not None:
            mensagem.config(
                text="Login realizado com sucesso!",
                fg="#3b9875"
            )
        else:
            mensagem.config(text="E-mail ou senha incorretos.")

    # Botão de login
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
