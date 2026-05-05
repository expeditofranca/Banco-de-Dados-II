CREATE DATABASE atividade_db
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

CREATE USER atividade_user WITH PASSWORD 'atividade123';

GRANT ALL PRIVILEGES ON DATABASE atividade_db TO atividade_user;

\c atividade_db;

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