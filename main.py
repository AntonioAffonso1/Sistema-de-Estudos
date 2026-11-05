
import tkinter as tk


# Paleta de cores
FUNDO = "#f4f6fb"


class SistemaDeEstudos:

    def __init__(self):
        self.janela = tk.Tk()

        self.janela.title("Sistema de Estudos")
        self.janela.geometry("1000x650")
        self.janela.configure(bg=FUNDO)

        self.janela.resizable(False, False)

    def executar(self):
        from interface.login import telaLogin

        telaLogin(self.janela)

        self.janela.mainloop()


# Inicialização
if __name__ == "__main__":
    programa = SistemaDeEstudos()
    programa.executar()
