# Sistema de Estudos

Aplicação desktop desenvolvida em Python para auxiliar estudantes na organização de tarefas, disciplinas e rotinas de estudo. O sistema possui interface gráfica, autenticação de usuários e integração com banco de dados Oracle.

**Versão:** 0.3.0  
**Status:** Projeto finalizado  
**Linguagem:** Python

---

## 1. Apresentação

O Sistema de Estudos foi desenvolvido com o propósito de oferecer uma ferramenta para auxiliar estudantes no gerenciamento de suas atividades acadêmicas.

A aplicação reúne diferentes recursos de organização em um único ambiente, permitindo cadastrar disciplinas, controlar tarefas, montar uma grade semanal de estudos, produzir resumos e criar flashcards para auxiliar na aprendizagem.

O sistema também possui autenticação de usuários, permitindo que diferentes estudantes utilizem a aplicação sem compartilhar seus dados pessoais e acadêmicos.

## 2. Funcionalidades

### 2.1. Cadastro e autenticação

- Cadastro de estudantes com nome, e-mail e senha.
- Login utilizando e-mail e senha.
- Identificação do estudante conectado.
- Separação dos dados de cada usuário.

### 2.2. Disciplinas

Permite organizar as matérias estudadas pelo usuário.

- Cadastrar disciplinas com nome e descrição.
- Editar informações cadastradas.
- Excluir disciplinas.
- Visualizar a lista de disciplinas.

### 2.3. Tarefas

Permite registrar e acompanhar atividades acadêmicas.

Cada tarefa possui:
- Nome;
- Descrição;
- Disciplina relacionada;
- Prioridade;
- Prazo;
- Status.

Operações disponíveis:
- Adicionar tarefas;
- Editar tarefas;
- Excluir tarefas;
- Marcar tarefas como concluídas.

Os status utilizados são:
- Pendente;
- Em andamento;
- Concluída.

### 2.4. Grade de estudos

Disponibiliza uma grade semanal para organizar os horários de estudo.

- Cinco dias da semana, de segunda a sexta-feira.
- Cinco horários por dia.
- Inclusão de atividades nos horários.
- Remoção de atividades.
- Salvamento da grade no banco de dados.

### 2.5. Resumos

Permite armazenar conteúdos de estudo separados por disciplina.

- Criar resumos com título e conteúdo.
- Associar resumos a disciplinas.
- Editar informações.
- Excluir resumos.

### 2.6. Flashcards

Recurso destinado à revisão e memorização de conteúdos.

- Criar cartões com perguntas e respostas.
- Associar cartões a disciplinas.
- Vincular flashcards a resumos, quando desejado.
- Editar e excluir cartões.

### 2.7. Estatísticas

Apresenta informações sobre o andamento das atividades acadêmicas.

- Quantidade total de tarefas.
- Quantidade de tarefas pendentes.
- Quantidade de tarefas em andamento.
- Quantidade de tarefas concluídas.
- Percentual de conclusão.
- Distribuição das tarefas por disciplina.

---

## 3. Tecnologias utilizadas

| Tecnologia | Aplicação |
|---|---|
| Python | Linguagem principal |
| Tkinter | Interface gráfica |
| Oracle Database XE 21c | Banco de dados relacional |
| python-oracledb | Comunicação entre Python e Oracle |
| SQL | Manipulação e gerenciamento dos dados |

### Conceitos aplicados

Durante o desenvolvimento foram utilizados conceitos de:

- Programação Orientada a Objetos;
- Classes, atributos e métodos;
- Modularização;
- Estruturas condicionais e de repetição;
- Listas e matrizes;
- Funções;
- Tratamento de exceções (`try` e `except`);
- Operações CRUD (Create, Read, Update e Delete);
- Modelagem de dados e relacionamentos;
- Chaves primárias e estrangeiras.

---

## 4. Estrutura de arquivos

O projeto está organizado da seguinte maneira:

```text
Trabalho-Interdisciplinar/
│
├── main.py
│
├── classes/
│   ├── __init__.py
│   ├── estudante.py
│   ├── tarefa.py
│   ├── grade_estudo.py
│   ├── resumo.py
│   ├── flashcard.py
│   └── disciplina.py
│
├── interface/
│   ├── __init__.py
│   ├── login.py
│   ├── cadastro.py
│   ├── inicio.py
│   ├── tarefas.py
│   ├── grade.py
│   ├── estatisticas.py
│   ├── disciplinas.py
│   ├── resumos.py
│   └── flashcards.py
│
├── servicos/
│   ├── __init__.py
│   ├── autenticacao.py
│   ├── disciplinas.py
│   ├── tarefas.py
│   ├── grade.py
│   ├── resumos.py
│   └── flashcards.py
│
├── banco/
│   └── conexao.py
│
├── teste_classes.py
│
└── .venv/
```

### Responsabilidade de cada diretório

**classes/**

Contém as classes responsáveis por representar os elementos do sistema, como estudantes, tarefas, disciplinas, resumos, flashcards e grades de estudo.

**interface/**

Contém as telas gráficas desenvolvidas com Tkinter. Cada arquivo representa uma parte da aplicação.

**servicos/**

Responsável pelas operações realizadas no banco de dados, incluindo cadastro, consulta, edição e exclusão de informações.

**banco/**

Armazena o código responsável pela conexão com o Oracle Database.

**main.py**

Arquivo responsável por iniciar a aplicação.

---

## 5. Banco de dados

O projeto utiliza o Oracle Database XE 21c para armazenar os dados de maneira persistente.

O banco possui sete tabelas principais:

| Tabela | Responsabilidade |
|---|---|
| ESTUDANTE | Armazena os dados dos usuários. |
| DISCIPLINA | Armazena as disciplinas de cada estudante. |
| TAREFA | Armazena as atividades acadêmicas. |
| RESUMO | Armazena os resumos cadastrados. |
| FLASHCARD | Armazena perguntas e respostas para revisão. |
| GRADE | Representa a grade de estudos de cada estudante. |
| HORARIOGRADE | Armazena as atividades de cada horário da grade. |

### Relacionamentos

- Um estudante pode possuir várias disciplinas.
- Um estudante pode possuir várias tarefas por meio de suas disciplinas.
- Um estudante pode possuir vários resumos por meio de suas disciplinas.
- Um estudante pode possuir vários flashcards por meio de suas disciplinas.
- Um estudante possui uma grade de estudos.
- Uma grade possui vários horários.
- Um resumo pode estar relacionado a vários flashcards.

As chaves primárias, estrangeiras e restrições de unicidade são utilizadas para manter a integridade dos registros.

---

## 6. Requisitos para instalação

Antes de executar o projeto, é necessário possuir:

- Windows 64 bits;
- Python instalado;
- Oracle Database XE 21c instalado e configurado;
- Usuário criado no banco de dados com as permissões necessárias;
- Biblioteca `oracledb` instalada no ambiente Python.

O projeto foi desenvolvido e testado utilizando Python 3.14 e Oracle Database XE 21c.

---

## 7. Configuração do ambiente

### 7.1. Obter o projeto

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta:

```bash
cd Trabalho-Interdisciplinar
```

### 7.2. Criar o ambiente virtual

No terminal do projeto, execute:

```bash
python -m venv .venv
```

Ative o ambiente virtual no PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 7.3. Instalar a biblioteca necessária

Com o ambiente virtual ativado, execute:

```bash
python -m pip install oracledb
```

---

## 8. Configuração do Oracle Database

O sistema utiliza uma conexão local com o Oracle Database.

As configurações de conexão estão no arquivo:

```text
banco/conexao.py
```

O modelo de conexão utilizado é:

```python
import oracledb

def conectar():
    try:
        conexao = oracledb.connect(
            user="SEU_USUARIO",
            password="SUA_SENHA",
            dsn="localhost:1521/XEPDB1"
        )
        return conexao

    except Exception as erro:
        print("Erro ao conectar com Oracle:", erro)
        return None
```

Substitua os valores de usuário e senha pelas credenciais do banco configurado localmente.

**Importante:** antes de executar a aplicação, é necessário criar o usuário e as sete tabelas descritas na seção anterior. O banco de dados deve estar iniciado e disponível no serviço `XEPDB1`.

Não compartilhe credenciais do banco de dados no repositório público.

---

## 9. Executando o sistema

Após configurar o ambiente Python e o banco de dados:

1. Abra o terminal na pasta principal do projeto.
2. Ative o ambiente virtual.
3. Verifique se o Oracle Database está em execução.
4. Execute o arquivo principal:

```bash
python main.py
```

A tela de login será apresentada. O usuário poderá acessar sua conta ou realizar um novo cadastro.

---

## 10. Como utilizar

### Primeiro acesso

1. Abra o sistema.
2. Selecione a opção de cadastro.
3. Informe nome, e-mail e senha.
4. Após o cadastro, retorne à tela de login.
5. Entre utilizando as credenciais cadastradas.

### Tela inicial

Após a autenticação, o usuário terá acesso ao menu principal, que apresenta as seguintes opções:

- Disciplinas;
- Tarefas;
- Grade de estudos;
- Estatísticas;
- Resumos;
- Flashcards.

### Fluxo recomendado de utilização

Para aproveitar os recursos do sistema, recomenda-se seguir esta ordem:

1. Cadastre as disciplinas que fazem parte da sua rotina.
2. Adicione tarefas e defina seus prazos e prioridades.
3. Organize seus horários na grade de estudos.
4. Registre resumos para armazenar conteúdos importantes.
5. Crie flashcards para revisar os assuntos estudados.
6. Consulte as estatísticas para acompanhar seu progresso.

Os dados cadastrados são armazenados no Oracle Database e permanecem disponíveis após fechar e abrir novamente a aplicação.

---

## 11. Observações e limitações

- O sistema depende de uma conexão ativa com o Oracle Database para realizar as operações de armazenamento e consulta.
- Cada estudante possui seus próprios registros, separados por meio dos relacionamentos do banco de dados.
- A grade de estudos possui cinco dias e cinco horários por dia.
- A aplicação foi desenvolvida com finalidade acadêmica e demonstrativa.
- O armazenamento atual de senhas utiliza texto sem hash. Portanto, não é recomendado utilizar senhas reais ou reutilizadas de outros serviços.
- A aplicação ainda não deve ser considerada pronta para implantação em ambiente de produção.

---

## 12. Versão do projeto

**Sistema de Estudos — v0.3.0**

Esta versão representa a entrega final do projeto acadêmico, reunindo os recursos de organização de estudos, gerenciamento de atividades, interface gráfica e integração com banco de dados relacional.

O desenvolvimento permitiu aplicar conhecimentos de programação, orientação a objetos, modelagem de dados, SQL e desenvolvimento de aplicações desktop.

---

## 13. Licença

Projeto desenvolvido para fins acadêmicos.
