# inicio do codigo aqui.


import tkinter as tk





# Paleta de cores
AZUL_PRINCIPAL = "#182c73"
AZUL_SECUNDARIO = "#15255e"
AZUL_BOTOES = "#3d4c82"

FUNDO = "#f4f6fb"
BRANCO = "#ffffff"
TEXTO = "#202a44"


class SistemaDeEstudos:

    def __init__(self):
        self.janela = tk.Tk()

        self.janela.title("Sistema de Estudos")
        self.janela.geometry("1000x650")
        self.janela.configure(bg=FUNDO)

        self.janela.resizable(False, False)

        self.criar_interface()

    def criar_interface(self):

        # Cabeçalho
        cabecalho = tk.Frame(
            self.janela,
            bg=AZUL_PRINCIPAL,
            height=80
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
        titulo.pack(side="left", padx=30, pady=20)

        # Área principal
        conteudo = tk.Frame(
            self.janela,
            bg=FUNDO
        )
        conteudo.pack(fill="both", expand=True, padx=30, pady=30)

        mensagem = tk.Label(
            conteudo,
            text="Bem-vindo ao Sistema de Estudos!",
            font=("Arial", 20, "bold"),
            bg=FUNDO,
            fg=TEXTO
        )
        mensagem.pack(anchor="w", pady=10)

        descricao = tk.Label(
            conteudo,
            text="Organize suas tarefas e sua rotina de estudos.",
            font=("Arial", 12),
            bg=FUNDO,
            fg="#7b8499"
        )
        descricao.pack(anchor="w")

    def executar(self):
        self.janela.mainloop()


# Inicialização
if __name__ == "__main__":
    from interface.login import telaLogin
    programa = SistemaDeEstudos()
    telaLogin(programa.janela)
    programa.executar()
