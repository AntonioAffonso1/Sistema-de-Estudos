
-- =========================================
-- INSERINDO ESTUDANTES
-- =========================================

INSERT INTO estudante (nome, email, senha)
VALUES ('Joao Silva', 'joao@email.com', 'senha123');

INSERT INTO estudante (nome, email, senha)
VALUES ('Maria Souza', 'maria@email.com', 'senha456');


-- CONFIRMANDO OS REGISTROS

SELECT * FROM estudante;

COMMIT;


-- =========================================
-- INSERINDO DISCIPLINAS
-- =========================================

INSERT INTO disciplina (nome, desc_disciplina, id_estudante)
VALUES ('Matematica', 'Estudos de matematica', 1);

INSERT INTO disciplina (nome, desc_disciplina, id_estudante)
VALUES ('Programacao', 'Estudos de programacao', 1);

INSERT INTO disciplina (nome, desc_disciplina, id_estudante)
VALUES ('Redes de Computadores', 'Estudos de redes', 2);


-- CONFIRMANDO OS REGISTROS

SELECT * FROM disciplina;

COMMIT;

INSERT INTO tarefa
(titulo_tarefa, descricao, data_prazo, prioridade, status, id_disciplina)
VALUES
('Estudar equacoes',
 'Revisar conceitos e resolver exemplos de equacoes.',
 TO_DATE('2026-11-10', 'YYYY-MM-DD'),
 'Alta',
 'Pendente',
 1);

INSERT INTO tarefa
(titulo_tarefa, descricao, data_prazo, prioridade, status, id_disciplina)
VALUES
('Resolver exercicios',
 'Resolver a lista de exercicios de matematica.',
 TO_DATE('2026-11-15', 'YYYY-MM-DD'),
 'Media',
 'Pendente',
 1);

INSERT INTO tarefa
(titulo_tarefa, descricao, data_prazo, prioridade, status, id_disciplina)
VALUES
('Praticar Python',
 'Desenvolver pequenos programas para praticar Python.',
 TO_DATE('2026-11-20', 'YYYY-MM-DD'),
 'Alta',
 'Em andamento',
 2);

SELECT * FROM tarefa;

COMMIT;

INSERT INTO resumo
(titulo_resumo, conteudo, id_disciplina)
VALUES
('Equacoes matematicas',
 'Uma equacao e uma igualdade matematica que possui uma ou mais incognitas. O objetivo e encontrar os valores que tornam a igualdade verdadeira.',
 1);

INSERT INTO resumo
(titulo_resumo, conteudo, id_disciplina)
VALUES
('Introducao ao Python',
 'Python e uma linguagem de programacao utilizada para desenvolver sistemas, automatizar tarefas e trabalhar com dados. Sua sintaxe e conhecida por ser simples e legivel.',
 2);

SELECT * FROM resumo;

COMMIT;

INSERT INTO flashcard
(pergunta, resposta, id_disciplina, id_resumo)
VALUES
('O que e uma variavel?',
 'Espaco utilizado para armazenar um valor.',
 2,
 2);

INSERT INTO flashcard
(pergunta, resposta, id_disciplina, id_resumo)
VALUES
('O que e uma equacao?',
 'Igualdade entre duas expressoes matematicas.',
 1,
 1);

INSERT INTO flashcard
(pergunta, resposta, id_disciplina, id_resumo)
VALUES
('O que e um algoritmo?',
 'Sequencia de passos para resolver um problema.',
 2,
 NULL);

SELECT * FROM flashcard;

COMMIT;


INSERT INTO grade (id_estudante)
VALUES (1);

INSERT INTO grade (id_estudante)
VALUES (2);

SELECT * FROM grade;

COMMIT;


-- Grade do estudante 1
INSERT INTO horarioGrade (id_grade, dia, horario, atividade)
VALUES (1, 'Segunda-feira', 1, 'Matematica');

INSERT INTO horarioGrade (id_grade, dia, horario, atividade)
VALUES (1, 'Terca-feira', 2, 'Programacao');

INSERT INTO horarioGrade (id_grade, dia, horario, atividade)
VALUES (1, 'Quarta-feira', 3, 'Revisao de matematica');

-- Grade do estudante 2
INSERT INTO horarioGrade (id_grade, dia, horario, atividade)
VALUES (2, 'Segunda-feira', 1, 'Redes de Computadores');

INSERT INTO horarioGrade (id_grade, dia, horario, atividade)
VALUES (2, 'Quinta-feira', 4, 'Estudo de redes');

SELECT * FROM horarioGrade;

COMMIT;

SELECT
    e.nome AS estudante,
    g.id_grade,
    hg.dia,
    hg.horario,
    hg.atividade
FROM estudante e
INNER JOIN grade g
    ON e.id_estudante = g.id_estudante
INNER JOIN horarioGrade hg
    ON g.id_grade = hg.id_grade
ORDER BY e.id_estudante, hg.dia, hg.horario;