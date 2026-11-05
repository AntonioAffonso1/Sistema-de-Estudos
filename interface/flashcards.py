
import tkinter as tk

from servicos.disciplinas import listarDisciplinas
from servicos.resumos import listarResumos

from servicos.flashcards import (
    listarFlashcards,
    adicionarFlashcard as salvarFlashcardBanco,
    editarFlashcard as atualizarFlashcardBanco,
    excluirFlashcard as removerFlashcardBanco
)


# Cores
AZUL_PRINCIPAL = "#182c73"
AZUL_SECUNDARIO = "#15255e"
AZUL_BOTOES = "#3d4c82"
FUNDO = "#f4f6fb"
BRANCO = "#ffffff"
TEXTO = "#202a44"
SUCESSO = "#3b9875"
ERRO = "#cf5c66"


def telaFlashcards(janela, estudante):

    # Preparação da tela
    for componente in janela.winfo_children():
        componente.destroy()

    janela.configure(bg=FUNDO)

    # Carrega os dados
    estudante.disciplinas = listarDisciplinas(estudante.id_estudante)
    estudante.resumos = listarResumos(estudante.id_estudante)
    estudante.flashcards = listarFlashcards(estudante.id_estudante)

    # Funções
    def voltar():
        from interface.inicio import telaInicio
        telaInicio(janela, estudante)

    def atualizarLista():
        listaFlashcards.delete(0, tk.END)

        for flashcard in estudante.flashcards:

            nomeDisciplina = "Sem disciplina"
            nomeResumo = "Sem resumo"

            for disciplina in estudante.disciplinas:
                if disciplina.id == flashcard.id_disciplina:
                    nomeDisciplina = disciplina.nome
                    break

            for resumo in estudante.resumos:
                if resumo.id_resumo == flashcard.id_resumo:
                    nomeResumo = resumo.titulo
                    break

            listaFlashcards.insert(
                tk.END,
                f"{flashcard.id_flashcard} | "
                f"{flashcard.pergunta} | "
                f"{nomeDisciplina} | "
                f"{nomeResumo}"
            )

    def limparCampos():
        campoPergunta.delete(0, tk.END)
        campoResposta.delete("1.0", tk.END)

        disciplinaSelecionada.set(nomesDisciplinas[0])
        resumoSelecionado.set(nomesResumos[0])

    def selecionarFlashcard(evento):
        try:
            selecao = listaFlashcards.curselection()

            if not selecao:
                return

            indice = selecao[0]
            flashcard = estudante.flashcards[indice]

            limparCampos()

            campoPergunta.insert(0, flashcard.pergunta)
            campoResposta.insert("1.0", flashcard.resposta)

            for disciplina in estudante.disciplinas:
                if disciplina.id == flashcard.id_disciplina:
                    disciplinaSelecionada.set(disciplina.nome)
                    break

            for resumo in estudante.resumos:
                if resumo.id_resumo == flashcard.id_resumo:
                    resumoSelecionado.set(resumo.titulo)
                    break

        except Exception as erro:
            print("Erro ao selecionar flashcard:", erro)

    def adicionarFlashcard():
        try:
            if not estudante.disciplinas:
                mensagem.config(
                    text="Cadastre uma disciplina primeiro.",
                    fg=ERRO
                )
                return

            pergunta = campoPergunta.get()
            resposta = campoResposta.get("1.0", tk.END).strip()

            if not pergunta or not resposta:
                mensagem.config(
                    text="Preencha a pergunta e a resposta.",
                    fg=ERRO
                )
                return

            disciplinaEncontrada = None

            for disciplina in estudante.disciplinas:
                if disciplina.nome == disciplinaSelecionada.get():
                    disciplinaEncontrada = disciplina
                    break

            if disciplinaEncontrada is None:
                mensagem.config(
                    text="Selecione uma disciplina válida.",
                    fg=ERRO
                )
                return

            idResumo = None

            if resumoSelecionado.get() != "Nenhum resumo associado":

                for resumo in estudante.resumos:
                    if resumo.titulo == resumoSelecionado.get():
                        idResumo = resumo.id_resumo
                        break

                if idResumo is None:
                    mensagem.config(
                        text="Selecione um resumo válido.",
                        fg=ERRO
                    )
                    return

            sucesso = salvarFlashcardBanco(
                pergunta,
                resposta,
                disciplinaEncontrada.id,
                idResumo,
                estudante.id_estudante
            )

            if sucesso:
                estudante.flashcards = listarFlashcards(
                    estudante.id_estudante
                )
                atualizarLista()
                limparCampos()

                mensagem.config(
                    text="Flashcard cadastrado com sucesso!",
                    fg=SUCESSO
                )
            else:
                mensagem.config(
                    text="Não foi possível cadastrar o flashcard.",
                    fg=ERRO
                )

        except Exception as erro:
            print("Erro ao cadastrar flashcard:", erro)
            mensagem.config(
                text="Não foi possível cadastrar o flashcard.",
                fg=ERRO
            )

    def editarFlashcard():
        try:
            selecao = listaFlashcards.curselection()

            if not selecao:
                mensagem.config(
                    text="Selecione um flashcard.",
                    fg=ERRO
                )
                return

            pergunta = campoPergunta.get()
            resposta = campoResposta.get("1.0", tk.END).strip()

            if not pergunta or not resposta:
                mensagem.config(
                    text="Preencha a pergunta e a resposta.",
                    fg=ERRO
                )
                return

            disciplinaEncontrada = None

            for disciplina in estudante.disciplinas:
                if disciplina.nome == disciplinaSelecionada.get():
                    disciplinaEncontrada = disciplina
                    break

            if disciplinaEncontrada is None:
                mensagem.config(
                    text="Selecione uma disciplina válida.",
                    fg=ERRO
                )
                return

            idResumo = None

            if resumoSelecionado.get() != "Nenhum resumo associado":

                for resumo in estudante.resumos:
                    if resumo.titulo == resumoSelecionado.get():
                        idResumo = resumo.id_resumo
                        break

                if idResumo is None:
                    mensagem.config(
                        text="Selecione um resumo válido.",
                        fg=ERRO
                    )
                    return

            indice = selecao[0]
            flashcard = estudante.flashcards[indice]

            sucesso = atualizarFlashcardBanco(
                flashcard.id_flashcard,
                pergunta,
                resposta,
                disciplinaEncontrada.id,
                idResumo,
                estudante.id_estudante
            )

            if sucesso:
                estudante.flashcards = listarFlashcards(
                    estudante.id_estudante
                )
                atualizarLista()
                limparCampos()

                mensagem.config(
                    text="Flashcard atualizado com sucesso!",
                    fg=SUCESSO
                )
            else:
                mensagem.config(
                    text="Não foi possível atualizar o flashcard.",
                    fg=ERRO
                )

        except Exception as erro:
            print("Erro ao editar flashcard:", erro)
            mensagem.config(
                text="Não foi possível editar o flashcard.",
                fg=ERRO
            )

    def excluirFlashcard():
        try:
            selecao = listaFlashcards.curselection()

            if not selecao:
                mensagem.config(
                    text="Selecione um flashcard.",
                    fg=ERRO
                )
                return

            indice = selecao[0]
            flashcard = estudante.flashcards[indice]

            sucesso = removerFlashcardBanco(
                flashcard.id_flashcard,
                estudante.id_estudante
            )

            if sucesso:
                estudante.flashcards = listarFlashcards(
                    estudante.id_estudante
                )
                atualizarLista()
                limparCampos()

                mensagem.config(
                    text="Flashcard excluído com sucesso!",
                    fg=SUCESSO
                )
            else:
                mensagem.config(
                    text="Não foi possível excluir o flashcard.",
                    fg=ERRO
                )

        except Exception as erro:
            print("Erro ao excluir flashcard:", erro)
            mensagem.config(
                text="Não foi possível excluir o flashcard.",
                fg=ERRO
            )

    # Cabeçalho
    cabecalho = tk.Frame(
        janela,
        bg=AZUL_PRINCIPAL,
        height=75
    )
    cabecalho.pack(fill="x")
    cabecalho.pack_propagate(False)

    tk.Label(
        cabecalho,
        text="Meus Flashcards",
        font=("Arial", 20, "bold"),
        bg=AZUL_PRINCIPAL,
        fg=BRANCO
    ).pack(side="left", padx=30, pady=20)

    tk.Button(
        cabecalho,
        text="Voltar",
        font=("Arial", 10, "bold"),
        bg=AZUL_BOTOES,
        fg=BRANCO,
        relief="flat",
        cursor="hand2",
        command=voltar
    ).pack(side="right", padx=30, pady=20)

    # Conteúdo principal
    conteudo = tk.Frame(janela, bg=FUNDO)
    conteudo.pack(fill="both", expand=True, padx=30, pady=15)

    # Formulário
    quadroFormulario = tk.Frame(
        conteudo,
        bg=BRANCO,
        padx=20,
        pady=10
    )
    quadroFormulario.pack(fill="x", pady=5)

    tk.Label(
        quadroFormulario,
        text="Cadastrar flashcard",
        font=("Arial", 15, "bold"),
        bg=BRANCO,
        fg=AZUL_PRINCIPAL
    ).pack(anchor="w", pady=(0, 5))

    tk.Label(
        quadroFormulario,
        text="Pergunta:",
        bg=BRANCO,
        fg=TEXTO
    ).pack(anchor="w")

    campoPergunta = tk.Entry(
        quadroFormulario,
        font=("Arial", 11)
    )
    campoPergunta.pack(fill="x", pady=(3, 5), ipady=4)

    tk.Label(
        quadroFormulario,
        text="Resposta:",
        bg=BRANCO,
        fg=TEXTO
    ).pack(anchor="w")

    campoResposta = tk.Text(
        quadroFormulario,
        font=("Arial", 10),
        height=3,
        wrap="word"
    )
    campoResposta.pack(fill="x", pady=(3, 5))

    # Seleção de disciplina
    tk.Label(
        quadroFormulario,
        text="Disciplina:",
        bg=BRANCO,
        fg=TEXTO
    ).pack(anchor="w")

    nomesDisciplinas = [
        disciplina.nome for disciplina in estudante.disciplinas
    ]

    if not nomesDisciplinas:
        nomesDisciplinas = ["Nenhuma disciplina cadastrada"]

    disciplinaSelecionada = tk.StringVar()
    disciplinaSelecionada.set(nomesDisciplinas[0])

    menuDisciplinas = tk.OptionMenu(
        quadroFormulario,
        disciplinaSelecionada,
        *nomesDisciplinas
    )
    menuDisciplinas.config(
        bg=BRANCO,
        fg=TEXTO,
        relief="solid"
    )
    menuDisciplinas.pack(anchor="w", pady=(3, 5))

    # Seleção de resumo
    tk.Label(
        quadroFormulario,
        text="Resumo relacionado (opcional):",
        bg=BRANCO,
        fg=TEXTO
    ).pack(anchor="w")

    nomesResumos = [
        resumo.titulo for resumo in estudante.resumos
    ]

    nomesResumos.insert(0, "Nenhum resumo associado")

    resumoSelecionado = tk.StringVar()
    resumoSelecionado.set(nomesResumos[0])

    menuResumos = tk.OptionMenu(
        quadroFormulario,
        resumoSelecionado,
        *nomesResumos
    )
    menuResumos.config(
        bg=BRANCO,
        fg=TEXTO,
        relief="solid"
    )
    menuResumos.pack(anchor="w", pady=(3, 5))

    # Lista de flashcards
    quadroLista = tk.Frame(
        conteudo,
        bg=BRANCO,
        padx=20,
        pady=10
    )
    quadroLista.pack(fill="both", expand=True, pady=5)

    tk.Label(
        quadroLista,
        text="Flashcards cadastrados",
        font=("Arial", 14, "bold"),
        bg=BRANCO,
        fg=AZUL_PRINCIPAL
    ).pack(anchor="w", pady=(0, 10))

    listaFlashcards = tk.Listbox(
        quadroLista,
        font=("Arial", 10),
        height=4,
        selectbackground=AZUL_BOTOES,
        selectforeground=BRANCO
    )
    listaFlashcards.pack(fill="both", expand=True)

    # Mensagem
    mensagem = tk.Label(
        conteudo,
        text="",
        font=("Arial", 10),
        bg=FUNDO
    )
    mensagem.pack(pady=3)

    listaFlashcards.bind(
        "<<ListboxSelect>>",
        selecionarFlashcard
    )

    # Botões
    botoes = tk.Frame(conteudo, bg=FUNDO)
    botoes.pack(fill="x", pady=3)

    tk.Button(
        botoes,
        text="Adicionar",
        bg=AZUL_PRINCIPAL,
        fg=BRANCO,
        relief="flat",
        cursor="hand2",
        width=15,
        command=adicionarFlashcard
    ).pack(side="left", padx=5)

    tk.Button(
        botoes,
        text="Editar",
        bg=AZUL_BOTOES,
        fg=BRANCO,
        relief="flat",
        cursor="hand2",
        width=15,
        command=editarFlashcard
    ).pack(side="left", padx=5)

    tk.Button(
        botoes,
        text="Excluir",
        bg="#cf5c66",
        fg=BRANCO,
        relief="flat",
        cursor="hand2",
        width=15,
        command=excluirFlashcard
    ).pack(side="left", padx=5)

    atualizarLista()
