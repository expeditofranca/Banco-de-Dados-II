CREATE DATABASE atividade_db
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

CREATE USER atividade_user WITH PASSWORD 'atividade123';

GRANT ALL PRIVILEGES ON DATABASE atividade_db TO atividade_user;