
import tkinter as tk

from classes.disciplina import Disciplina

AZUL_PRINCIPAL = "#182c73"
AZUL_SECUNDARIO = "#15255e"
AZUL_BOTOES = "#3d4c82"
FUNDO = "#f4f6fb"
BRANCO = "#ffffff"
TEXTO = "#202a44"


def telaDisciplinas(janela, estudante):

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
        text="Minhas disciplinas",
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
    conteudo.pack(fill="both", expand=True, padx=30, pady=20)

    # Área do formulário
    quadroFormulario = tk.Frame(
        conteudo,
        bg=BRANCO,
        padx=20,
        pady=15
    )
    quadroFormulario.pack(fill="x", pady=10)

    tk.Label(
        quadroFormulario,
        text="Cadastrar disciplina",
        font=("Arial", 15, "bold"),
        bg=BRANCO,
        fg=AZUL_PRINCIPAL
    ).pack(anchor="w", pady=(0, 10))

    tk.Label(
        quadroFormulario,
        text="Nome:",
        bg=BRANCO,
        fg=TEXTO
    ).pack(anchor="w")

    campoNome = tk.Entry(
        quadroFormulario,
        font=("Arial", 11)
    )
    campoNome.pack(fill="x", pady=(3, 10), ipady=5)

    tk.Label(
        quadroFormulario,
        text="Descrição:",
        bg=BRANCO,
        fg=TEXTO
    ).pack(anchor="w")

    campoDescricao = tk.Entry(
        quadroFormulario,
        font=("Arial", 11)
    )
    campoDescricao.pack(fill="x", pady=(3, 10), ipady=5)

    # Lista de disciplinas
    quadroLista = tk.Frame(
        conteudo,
        bg=BRANCO,
        padx=20,
        pady=15
    )
    quadroLista.pack(fill="both", expand=True, pady=10)

    tk.Label(
        quadroLista,
        text="Disciplinas cadastradas",
        font=("Arial", 14, "bold"),
        bg=BRANCO,
        fg=AZUL_PRINCIPAL
    ).pack(anchor="w", pady=(0, 10))

    listaDisciplinas = tk.Listbox(
        quadroLista,
        font=("Arial", 10),
        height=8,
        selectbackground=AZUL_BOTOES,
        selectforeground=BRANCO
    )
    listaDisciplinas.pack(fill="both", expand=True)

    mensagem = tk.Label(
        conteudo,
        text="",
        font=("Arial", 10),
        bg=FUNDO
    )
    mensagem.pack(pady=5)

    # Atualiza a lista
    def atualizarLista():

        listaDisciplinas.delete(0, tk.END)

        for disciplina in estudante.disciplinas:
            listaDisciplinas.insert(
                tk.END,
                f"{disciplina.id} | {disciplina.nome} | {disciplina.descricao}"
            )

    # Limpa os campos
    def limparCampos():

        campoNome.delete(0, tk.END)
        campoDescricao.delete(0, tk.END)

    # Seleciona uma disciplina
    def selecionarDisciplina(evento):

        try:
            selecao = listaDisciplinas.curselection()

            if not selecao:
                return

            indice = selecao[0]
            disciplina = estudante.disciplinas[indice]

            limparCampos()

            campoNome.insert(0, disciplina.nome)
            campoDescricao.insert(0, disciplina.descricao)

        except Exception as erro:
            print("Erro ao selecionar disciplina:", erro)

    listaDisciplinas.bind(
        "<<ListboxSelect>>",
        selecionarDisciplina
    )

    # Adiciona uma disciplina
    def adicionarDisciplina():

        try:
            nome = campoNome.get()
            descricao = campoDescricao.get()

            if not nome or not descricao:
                mensagem.config(
                    text="Preencha todos os campos.",
                    fg="#cf5c66"
                )
                return

            # Gera um novo identificador
            novoId = 1

            for disciplina in estudante.disciplinas:
                if disciplina.id >= novoId:
                    novoId = disciplina.id + 1

            novaDisciplina = Disciplina(
                novoId,
                nome,
                descricao
            )

            estudante.disciplinas.append(novaDisciplina)

            atualizarLista()
            limparCampos()

            mensagem.config(
                text="Disciplina cadastrada com sucesso!",
                fg="#3b9875"
            )

        except Exception as erro:
            print("Erro ao cadastrar disciplina:", erro)
            mensagem.config(
                text="Não foi possível cadastrar a disciplina.",
                fg="#cf5c66"
            )

    # Edita uma disciplina
    def editarDisciplina():

        try:
            selecao = listaDisciplinas.curselection()

            if not selecao:
                mensagem.config(
                    text="Selecione uma disciplina.",
                    fg="#cf5c66"
                )
                return

            nome = campoNome.get()
            descricao = campoDescricao.get()

            if not nome or not descricao:
                mensagem.config(
                    text="Preencha todos os campos.",
                    fg="#cf5c66"
                )
                return

            indice = selecao[0]
            disciplina = estudante.disciplinas[indice]

            disciplina.editar(nome, descricao)

            atualizarLista()
            limparCampos()

            mensagem.config(
                text="Disciplina editada com sucesso!",
                fg="#3b9875"
            )

        except Exception as erro:
            print("Erro ao editar disciplina:", erro)
            mensagem.config(
                text="Não foi possível editar a disciplina.",
                fg="#cf5c66"
            )

    # Exclui uma disciplina
    def excluirDisciplina():

        try:
            selecao = listaDisciplinas.curselection()

            if not selecao:
                mensagem.config(
                    text="Selecione uma disciplina.",
                    fg="#cf5c66"
                )
                return

            indice = selecao[0]

            estudante.disciplinas.pop(indice)

            atualizarLista()
            limparCampos()

            mensagem.config(
                text="Disciplina excluída com sucesso!",
                fg="#3b9875"
            )

        except Exception as erro:
            print("Erro ao excluir disciplina:", erro)
            mensagem.config(
                text="Não foi possível excluir a disciplina.",
                fg="#cf5c66"
            )

    # Botões
    botoes = tk.Frame(conteudo, bg=FUNDO)
    botoes.pack(fill="x", pady=5)

    tk.Button(
        botoes,
        text="Adicionar",
        bg=AZUL_PRINCIPAL,
        fg=BRANCO,
        relief="flat",
        cursor="hand2",
        width=15,
        command=adicionarDisciplina
    ).pack(side="left", padx=5)

    tk.Button(
        botoes,
        text="Editar",
        bg=AZUL_BOTOES,
        fg=BRANCO,
        relief="flat",
        cursor="hand2",
        width=15,
        command=editarDisciplina
    ).pack(side="left", padx=5)

    tk.Button(
        botoes,
        text="Excluir",
        bg="#cf5c66",
        fg=BRANCO,
        relief="flat",
        cursor="hand2",
        width=15,
        command=excluirDisciplina
    ).pack(side="left", padx=5)

    atualizarLista()
