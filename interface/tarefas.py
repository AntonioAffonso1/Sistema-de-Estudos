
import tkinter as tk

from servicos.disciplinas import listarDisciplinas

from servicos.tarefas import (
    listarTarefas,
    adicionarTarefa as salvarTarefa,
    editarTarefa as atualizarTarefaBanco,
    concluirTarefa as concluirTarefaBanco,
    excluirTarefa as excluirTarefaBanco
)


# Cores
AZUL_PRINCIPAL = "#182c73"
AZUL_SECUNDARIO = "#15255e"
AZUL_BOTOES = "#3d4c82"
FUNDO = "#f4f6fb"
BRANCO = "#ffffff"
TEXTO = "#202a44"


def telaTarefas(janela, estudante):

    # Preparação da tela
    for componente in janela.winfo_children():
        componente.destroy()

    janela.configure(bg=FUNDO)

    # Carrega os dados
    estudante.disciplinas = listarDisciplinas(estudante.id_estudante)

    # Funções
    def voltar():
        from interface.inicio import telaInicio
        telaInicio(janela, estudante)

    def atualizarLista():
        listaTarefas.delete(0, tk.END)

        estudante.tarefas = listarTarefas(estudante.id_estudante)

        for tarefa in estudante.tarefas:
            texto = (
                f"{tarefa.nome} | {tarefa.disciplina} | "
                f"{tarefa.prioridade} | {tarefa.prazo} | {tarefa.status}"
            )

            listaTarefas.insert(tk.END, texto)

    def limparCampos():
        campoNome.delete(0, tk.END)
        campoDescricao.delete(0, tk.END)
        campoDisciplina.delete(0, tk.END)
        campoPrioridade.delete(0, tk.END)
        campoPrazo.delete(0, tk.END)

    def adicionarTarefa():
        try:
            nome = campoNome.get()
            descricao = campoDescricao.get()
            disciplina = campoDisciplina.get()
            prioridade = campoPrioridade.get()
            prazo = campoPrazo.get()

            if not nome or not descricao or not disciplina or not prioridade or not prazo:
                mensagem.config(text="Preencha todos os campos.")
                return

            # Procura a disciplina cadastrada pelo estudante
            disciplinaEncontrada = None

            for item in estudante.disciplinas:
                if item.nome.lower() == disciplina.lower():
                    disciplinaEncontrada = item
                    break

            if disciplinaEncontrada is None:
                mensagem.config(
                    text="Disciplina não encontrada. Verifique o nome."
                )
                return

            sucesso = salvarTarefa(
                nome,
                descricao,
                disciplinaEncontrada.id,
                prioridade,
                prazo,
                estudante.id_estudante
            )

            if sucesso:
                atualizarLista()
                limparCampos()

                mensagem.config(
                    text="Tarefa adicionada com sucesso!",
                    fg="#3b9875"
                )
            else:
                mensagem.config(
                    text="Não foi possível adicionar a tarefa."
                )

        except Exception as erro:
            print("Erro ao adicionar tarefa:", erro)
            mensagem.config(text="Ocorreu um erro ao adicionar a tarefa.")

    def selecionarTarefa(evento):
        selecao = listaTarefas.curselection()

        if selecao:
            indice = selecao[0]
            tarefa = estudante.tarefas[indice]

            limparCampos()

            campoNome.insert(0, tarefa.nome)
            campoDescricao.insert(0, tarefa.descricao)
            campoDisciplina.insert(0, tarefa.disciplina)
            campoPrioridade.insert(0, tarefa.prioridade)
            campoPrazo.insert(0, tarefa.prazo)

            mensagem.config(text="Tarefa selecionada para edição.")

    def editarTarefa():
        try:
            selecao = listaTarefas.curselection()

            if not selecao:
                mensagem.config(text="Selecione uma tarefa para editar.")
                return

            nome = campoNome.get()
            descricao = campoDescricao.get()
            disciplina = campoDisciplina.get()
            prioridade = campoPrioridade.get()
            prazo = campoPrazo.get()

            if not nome or not descricao or not disciplina or not prioridade or not prazo:
                mensagem.config(text="Preencha todos os campos.")
                return

            indice = selecao[0]
            tarefa = estudante.tarefas[indice]

            disciplinaEncontrada = None

            for item in estudante.disciplinas:
                if item.nome.lower() == disciplina.lower():
                    disciplinaEncontrada = item
                    break

            if disciplinaEncontrada is None:
                mensagem.config(
                    text="Disciplina não encontrada. Verifique o nome."
                )
                return

            sucesso = atualizarTarefaBanco(
                tarefa.id_tarefa,
                nome,
                descricao,
                disciplinaEncontrada.id,
                prioridade,
                prazo,
                estudante.id_estudante
            )

            if sucesso:
                atualizarLista()
                limparCampos()

                mensagem.config(
                    text="Tarefa editada com sucesso!",
                    fg="#3b9875"
                )
            else:
                mensagem.config(
                    text="Não foi possível editar a tarefa."
                )

        except Exception as erro:
            print("Erro ao editar tarefa:", erro)
            mensagem.config(text="Ocorreu um erro ao editar a tarefa.")

    def concluirTarefa():
        try:
            selecao = listaTarefas.curselection()

            if not selecao:
                mensagem.config(text="Selecione uma tarefa.")
                return

            indice = selecao[0]
            tarefa = estudante.tarefas[indice]

            if tarefa.status == "Concluída":
                mensagem.config(text="Esta tarefa já foi concluída.")
                return

            sucesso = concluirTarefaBanco(
                tarefa.id_tarefa,
                estudante.id_estudante
            )

            if sucesso:
                atualizarLista()

                mensagem.config(
                    text="Tarefa concluída!",
                    fg="#3b9875"
                )
            else:
                mensagem.config(
                    text="Não foi possível concluir a tarefa."
                )

        except Exception as erro:
            print("Erro ao concluir tarefa:", erro)
            mensagem.config(text="Ocorreu um erro ao concluir a tarefa.")

    def excluirTarefa():
        try:
            selecao = listaTarefas.curselection()

            if not selecao:
                mensagem.config(text="Selecione uma tarefa.")
                return

            indice = selecao[0]
            tarefa = estudante.tarefas[indice]

            sucesso = excluirTarefaBanco(
                tarefa.id_tarefa,
                estudante.id_estudante
            )

            if sucesso:
                atualizarLista()
                limparCampos()

                mensagem.config(
                    text="Tarefa excluída com sucesso!",
                    fg="#3b9875"
                )
            else:
                mensagem.config(
                    text="Não foi possível excluir a tarefa."
                )

        except Exception as erro:
            print("Erro ao excluir tarefa:", erro)
            mensagem.config(text="Ocorreu um erro ao excluir a tarefa.")

    # Cabeçalho
    cabecalho = tk.Frame(janela, bg=AZUL_PRINCIPAL, height=75)
    cabecalho.pack(fill="x")
    cabecalho.pack_propagate(False)

    titulo = tk.Label(
        cabecalho,
        text="Minhas tarefas",
        font=("Arial", 20, "bold"),
        bg=AZUL_PRINCIPAL,
        fg=BRANCO
    )
    titulo.pack(side="left", padx=30, pady=20)

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

    # Conteúdo
    conteudo = tk.Frame(janela, bg=FUNDO)
    conteudo.pack(fill="both", expand=True, padx=30, pady=20)

    # Formulário
    formulario = tk.Frame(conteudo, bg=BRANCO, padx=20, pady=15)
    formulario.pack(fill="x", pady=(0, 15))

    tk.Label(
        formulario,
        text="Dados da tarefa",
        font=("Arial", 15, "bold"),
        bg=BRANCO,
        fg=AZUL_PRINCIPAL
    ).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))

    tk.Label(formulario, text="Nome:", bg=BRANCO, fg=TEXTO).grid(
        row=1, column=0, sticky="w", pady=5
    )
    campoNome = tk.Entry(formulario, width=35, font=("Arial", 11))
    campoNome.grid(row=1, column=1, sticky="w", pady=5)

    tk.Label(formulario, text="Descrição:", bg=BRANCO, fg=TEXTO).grid(
        row=2, column=0, sticky="w", pady=5
    )
    campoDescricao = tk.Entry(formulario, width=35, font=("Arial", 11))
    campoDescricao.grid(row=2, column=1, sticky="w", pady=5)

    tk.Label(formulario, text="Disciplina:", bg=BRANCO, fg=TEXTO).grid(
        row=3, column=0, sticky="w", pady=5
    )
    campoDisciplina = tk.Entry(formulario, width=35, font=("Arial", 11))
    campoDisciplina.grid(row=3, column=1, sticky="w", pady=5)

    tk.Label(formulario, text="Prioridade:", bg=BRANCO, fg=TEXTO).grid(
        row=4, column=0, sticky="w", pady=5
    )
    campoPrioridade = tk.Entry(formulario, width=35, font=("Arial", 11))
    campoPrioridade.grid(row=4, column=1, sticky="w", pady=5)

    tk.Label(
        formulario,
        text="Prazo (DD/MM/AAAA):",
        bg=BRANCO,
        fg=TEXTO
    ).grid(row=5, column=0, sticky="w", pady=5)

    campoPrazo = tk.Entry(formulario, width=35, font=("Arial", 11))
    campoPrazo.grid(row=5, column=1, sticky="w", pady=5)

    mensagem = tk.Label(
        formulario,
        text="",
        font=("Arial", 10),
        bg=BRANCO,
        fg="#cf5c66"
    )
    mensagem.grid(row=6, column=0, columnspan=2, pady=5)

    # Lista de tarefas
    areaLista = tk.Frame(conteudo, bg=BRANCO, padx=20, pady=15)
    areaLista.pack(fill="both", expand=True)

    tk.Label(
        areaLista,
        text="Suas atividades",
        font=("Arial", 15, "bold"),
        bg=BRANCO,
        fg=AZUL_PRINCIPAL
    ).pack(anchor="w", pady=(0, 10))

    listaTarefas = tk.Listbox(
        areaLista,
        font=("Arial", 11),
        height=8,
        selectbackground=AZUL_BOTOES,
        selectforeground=BRANCO
    )
    listaTarefas.pack(fill="both", expand=True)

    listaTarefas.bind("<<ListboxSelect>>", selecionarTarefa)

    # Botões
    botoes = tk.Frame(areaLista, bg=BRANCO)
    botoes.pack(fill="x", pady=12)

    tk.Button(
        botoes,
        text="Adicionar",
        bg=AZUL_PRINCIPAL,
        fg=BRANCO,
        relief="flat",
        cursor="hand2",
        command=adicionarTarefa
    ).pack(side="left", padx=5)

    tk.Button(
        botoes,
        text="Editar",
        bg=AZUL_BOTOES,
        fg=BRANCO,
        relief="flat",
        cursor="hand2",
        command=editarTarefa
    ).pack(side="left", padx=5)

    tk.Button(
        botoes,
        text="Concluir",
        bg=AZUL_BOTOES,
        fg=BRANCO,
        relief="flat",
        cursor="hand2",
        command=concluirTarefa
    ).pack(side="left", padx=5)

    tk.Button(
        botoes,
        text="Excluir",
        bg="#cf5c66",
        fg=BRANCO,
        relief="flat",
        cursor="hand2",
        command=excluirTarefa
    ).pack(side="left", padx=5)

    atualizarLista()
