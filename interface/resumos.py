
import tkinter as tk

from servicos.disciplinas import listarDisciplinas

from servicos.resumos import (
    listarResumos,
    adicionarResumo as salvarResumoBanco,
    editarResumo as atualizarResumoBanco,
    excluirResumo as removerResumoBanco
)


# Cores
AZUL_PRINCIPAL = "#182c73"
AZUL_SECUNDARIO = "#15255e"
AZUL_BOTOES = "#3d4c82"
FUNDO = "#f4f6fb"
BRANCO = "#ffffff"
TEXTO = "#202a44"


def telaResumos(janela, estudante):

    # Preparação da tela
    for componente in janela.winfo_children():
        componente.destroy()

    janela.configure(bg=FUNDO)

    # Carrega os dados
    estudante.disciplinas = listarDisciplinas(estudante.id_estudante)
    estudante.resumos = listarResumos(estudante.id_estudante)

    # Funções
    def voltar():
        from interface.inicio import telaInicio
        telaInicio(janela, estudante)

    def atualizarLista():
        listaResumos.delete(0, tk.END)

        for resumo in estudante.resumos:

            nomeDisciplina = "Sem disciplina"

            for disciplina in estudante.disciplinas:
                if disciplina.id == resumo.id_disciplina:
                    nomeDisciplina = disciplina.nome
                    break

            listaResumos.insert(
                tk.END,
                f"{resumo.id_resumo} | {resumo.titulo} | {nomeDisciplina}"
            )

    def limparCampos():
        campoTitulo.delete(0, tk.END)
        campoConteudo.delete("1.0", tk.END)

        if nomesDisciplinas:
            disciplinaSelecionada.set(nomesDisciplinas[0])

    def selecionarResumo(evento):
        try:
            selecao = listaResumos.curselection()

            if not selecao:
                return

            indice = selecao[0]
            resumo = estudante.resumos[indice]

            limparCampos()

            campoTitulo.insert(0, resumo.titulo)
            campoConteudo.insert("1.0", resumo.conteudo)

            for disciplina in estudante.disciplinas:
                if disciplina.id == resumo.id_disciplina:
                    disciplinaSelecionada.set(disciplina.nome)
                    break

        except Exception as erro:
            print("Erro ao selecionar resumo:", erro)

    def adicionarResumo():
        try:
            if not estudante.disciplinas:
                mensagem.config(
                    text="Cadastre uma disciplina primeiro.",
                    fg="#cf5c66"
                )
                return

            titulo = campoTitulo.get()
            conteudoResumo = campoConteudo.get("1.0", tk.END).strip()
            nomeDisciplina = disciplinaSelecionada.get()

            if not titulo or not conteudoResumo:
                mensagem.config(
                    text="Preencha todos os campos.",
                    fg="#cf5c66"
                )
                return

            disciplinaEncontrada = None

            for disciplina in estudante.disciplinas:
                if disciplina.nome == nomeDisciplina:
                    disciplinaEncontrada = disciplina
                    break

            if disciplinaEncontrada is None:
                mensagem.config(
                    text="Selecione uma disciplina válida.",
                    fg="#cf5c66"
                )
                return

            sucesso = salvarResumoBanco(
                titulo,
                conteudoResumo,
                disciplinaEncontrada.id,
                estudante.id_estudante
            )

            if sucesso:
                estudante.resumos = listarResumos(estudante.id_estudante)

                atualizarLista()
                limparCampos()

                mensagem.config(
                    text="Resumo cadastrado com sucesso!",
                    fg="#3b9875"
                )
            else:
                mensagem.config(
                    text="Não foi possível cadastrar o resumo.",
                    fg="#cf5c66"
                )

        except Exception as erro:
            print("Erro ao cadastrar resumo:", erro)
            mensagem.config(
                text="Não foi possível cadastrar o resumo.",
                fg="#cf5c66"
            )

    def editarResumo():
        try:
            selecao = listaResumos.curselection()

            if not selecao:
                mensagem.config(
                    text="Selecione um resumo.",
                    fg="#cf5c66"
                )
                return

            titulo = campoTitulo.get()
            conteudoResumo = campoConteudo.get("1.0", tk.END).strip()

            if not titulo or not conteudoResumo:
                mensagem.config(
                    text="Preencha todos os campos.",
                    fg="#cf5c66"
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
                    fg="#cf5c66"
                )
                return

            indice = selecao[0]
            resumo = estudante.resumos[indice]

            sucesso = atualizarResumoBanco(
                resumo.id_resumo,
                titulo,
                conteudoResumo,
                disciplinaEncontrada.id,
                estudante.id_estudante
            )

            if sucesso:
                estudante.resumos = listarResumos(estudante.id_estudante)

                atualizarLista()
                limparCampos()

                mensagem.config(
                    text="Resumo editado com sucesso!",
                    fg="#3b9875"
                )
            else:
                mensagem.config(
                    text="Não foi possível editar o resumo.",
                    fg="#cf5c66"
                )

        except Exception as erro:
            print("Erro ao editar resumo:", erro)
            mensagem.config(
                text="Não foi possível editar o resumo.",
                fg="#cf5c66"
            )

    def excluirResumo():
        try:
            selecao = listaResumos.curselection()

            if not selecao:
                mensagem.config(
                    text="Selecione um resumo.",
                    fg="#cf5c66"
                )
                return

            indice = selecao[0]
            resumo = estudante.resumos[indice]

            sucesso = removerResumoBanco(
                resumo.id_resumo,
                estudante.id_estudante
            )

            if sucesso:
                estudante.resumos = listarResumos(estudante.id_estudante)

                atualizarLista()
                limparCampos()

                mensagem.config(
                    text="Resumo excluído com sucesso!",
                    fg="#3b9875"
                )
            else:
                mensagem.config(
                    text="Não foi possível excluir o resumo.",
                    fg="#cf5c66"
                )

        except Exception as erro:
            print("Erro ao excluir resumo:", erro)
            mensagem.config(
                text="Não foi possível excluir o resumo.",
                fg="#cf5c66"
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
        text="Meus resumos",
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
    conteudo.pack(fill="both", expand=True, padx=30, pady=20)

    # Formulário
    quadroFormulario = tk.Frame(
        conteudo,
        bg=BRANCO,
        padx=20,
        pady=10
    )
    quadroFormulario.pack(fill="x", pady=10)

    tk.Label(
        quadroFormulario,
        text="Cadastrar resumo",
        font=("Arial", 15, "bold"),
        bg=BRANCO,
        fg=AZUL_PRINCIPAL
    ).pack(anchor="w", pady=(0, 10))

    tk.Label(
        quadroFormulario,
        text="Título:",
        bg=BRANCO,
        fg=TEXTO
    ).pack(anchor="w")

    campoTitulo = tk.Entry(
        quadroFormulario,
        font=("Arial", 11)
    )
    campoTitulo.pack(fill="x", pady=(3, 10), ipady=5)

    tk.Label(
        quadroFormulario,
        text="Conteúdo:",
        bg=BRANCO,
        fg=TEXTO
    ).pack(anchor="w")

    campoConteudo = tk.Text(
        quadroFormulario,
        font=("Arial", 10),
        height=3,
        wrap="word"
    )
    campoConteudo.pack(fill="x", pady=(3, 10))

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
    menuDisciplinas.pack(anchor="w", pady=(3, 10))

    # Lista de resumos
    quadroLista = tk.Frame(
        conteudo,
        bg=BRANCO,
        padx=20,
        pady=10
    )
    quadroLista.pack(fill="x", pady=5)

    tk.Label(
        quadroLista,
        text="Resumos cadastrados",
        font=("Arial", 14, "bold"),
        bg=BRANCO,
        fg=AZUL_PRINCIPAL
    ).pack(anchor="w", pady=(0, 10))

    listaResumos = tk.Listbox(
        quadroLista,
        font=("Arial", 10),
        height=4,
        selectbackground=AZUL_BOTOES,
        selectforeground=BRANCO
    )
    listaResumos.pack(fill="x")

    # Mensagem
    mensagem = tk.Label(
        conteudo,
        text="",
        font=("Arial", 10),
        bg=FUNDO
    )
    mensagem.pack(pady=5)

    listaResumos.bind(
        "<<ListboxSelect>>",
        selecionarResumo
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
        command=adicionarResumo
    ).pack(side="left", padx=5)

    tk.Button(
        botoes,
        text="Editar",
        bg=AZUL_BOTOES,
        fg=BRANCO,
        relief="flat",
        cursor="hand2",
        width=15,
        command=editarResumo
    ).pack(side="left", padx=5)

    tk.Button(
        botoes,
        text="Excluir",
        bg="#cf5c66",
        fg=BRANCO,
        relief="flat",
        cursor="hand2",
        width=15,
        command=excluirResumo
    ).pack(side="left", padx=5)

    atualizarLista()
