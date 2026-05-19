\c atividade_bd;

CREATE TABLE projeto (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    lider VARCHAR(100)
);

-- cria tabela de atividades
CREATE TABLE atividade (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(100),
    descricao TEXT,
    projeto_id INT,
    FOREIGN KEY (projeto_id) REFERENCES projeto(id)
);