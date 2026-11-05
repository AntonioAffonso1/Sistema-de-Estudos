
-- =========================================
-- 1. TABELA ESTUDANTE
-- =========================================

CREATE TABLE estudante (
    id_estudante NUMBER GENERATED ALWAYS AS IDENTITY,
    nome VARCHAR2(150) NOT NULL,
    email VARCHAR2(150) NOT NULL,
    senha VARCHAR2(255) NOT NULL,

    CONSTRAINT pk_estudante PRIMARY KEY (id_estudante),
    CONSTRAINT uk_estudante_email UNIQUE (email)
);


-- =========================================
-- 2. TABELA DISCIPLINA
-- =========================================

CREATE TABLE disciplina (
    id_disciplina NUMBER GENERATED ALWAYS AS IDENTITY,
    nome VARCHAR2(150) NOT NULL,
    desc_disciplina VARCHAR2(150) NOT NULL,
    id_estudante NUMBER NOT NULL,

    CONSTRAINT pk_disciplina PRIMARY KEY (id_disciplina),

    CONSTRAINT fk_estudante_disciplina
        FOREIGN KEY (id_estudante)
        REFERENCES estudante(id_estudante)
);


-- =========================================
-- 3. TABELA TAREFA
-- =========================================

CREATE TABLE tarefa (
    id_tarefa NUMBER GENERATED ALWAYS AS IDENTITY,
    titulo_tarefa VARCHAR2(150) NOT NULL,
    descricao VARCHAR2(500) NOT NULL,
    data_prazo DATE NOT NULL,
    prioridade VARCHAR2(10) NOT NULL,
    status VARCHAR2(20) NOT NULL,
    id_disciplina NUMBER NOT NULL,

    CONSTRAINT pk_tarefa PRIMARY KEY (id_tarefa),

    CONSTRAINT fk_disciplina_tarefa
        FOREIGN KEY (id_disciplina)
        REFERENCES disciplina(id_disciplina)
);


-- =========================================
-- 4. TABELA RESUMO
-- =========================================

CREATE TABLE resumo (
    id_resumo NUMBER GENERATED ALWAYS AS IDENTITY,
    titulo_resumo VARCHAR2(150) NOT NULL,
    conteudo VARCHAR2(4000) NOT NULL,
    id_disciplina NUMBER NOT NULL,

    CONSTRAINT pk_resumo PRIMARY KEY (id_resumo),

    CONSTRAINT fk_disciplina_resumo
        FOREIGN KEY (id_disciplina)
        REFERENCES disciplina(id_disciplina)
);


-- =========================================
-- 5. TABELA FLASHCARD
-- =========================================

CREATE TABLE flashcard (
    id_flashcard NUMBER GENERATED ALWAYS AS IDENTITY,
    pergunta VARCHAR2(150) NOT NULL,
    resposta VARCHAR2(200) NOT NULL,
    id_disciplina NUMBER NOT NULL,
    id_resumo NUMBER,

    CONSTRAINT pk_flashcard PRIMARY KEY (id_flashcard),

    CONSTRAINT fk_disciplina_flashcard
        FOREIGN KEY (id_disciplina)
        REFERENCES disciplina(id_disciplina),

    CONSTRAINT fk_resumo_flashcard
        FOREIGN KEY (id_resumo)
        REFERENCES resumo(id_resumo)
);


-- =========================================
-- 6. TABELA GRADE
-- =========================================

CREATE TABLE grade (
    id_grade NUMBER GENERATED ALWAYS AS IDENTITY,
    id_estudante NUMBER NOT NULL,

    CONSTRAINT pk_grade PRIMARY KEY (id_grade),

    CONSTRAINT fk_grade_estudante
        FOREIGN KEY (id_estudante)
        REFERENCES estudante(id_estudante),

    CONSTRAINT uk_grade_estudante UNIQUE (id_estudante)
);


-- =========================================
-- 7. TABELA HORARIOGRADE
-- =========================================

CREATE TABLE horarioGrade (
    id_horarioGrade NUMBER GENERATED ALWAYS AS IDENTITY,
    id_grade NUMBER NOT NULL,
    dia VARCHAR2(20) NOT NULL,
    horario NUMBER(1) NOT NULL,
    atividade VARCHAR2(200) NOT NULL,

    CONSTRAINT pk_horarioGrade PRIMARY KEY (id_horarioGrade),

    CONSTRAINT fk_horarioGrade_grade
        FOREIGN KEY (id_grade)
        REFERENCES grade(id_grade),

    CONSTRAINT ck_horario_aula
        CHECK (horario BETWEEN 1 AND 5),

    CONSTRAINT uk_horario_grade
        UNIQUE (id_grade, dia, horario)
);

SELECT table_name
FROM user_tables
ORDER BY table_name;