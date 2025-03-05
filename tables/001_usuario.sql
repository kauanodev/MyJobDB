-- Table: public.Usuario

-- DROP TABLE IF EXISTS public."Usuario";

CREATE TABLE IF NOT EXISTS public."Usuario"
(
    id integer NOT NULL,
    cpf character varying(11) COLLATE pg_catalog."default" NOT NULL,
    endereco text COLLATE pg_catalog."default" NOT NULL,
    nome character varying(255) COLLATE pg_catalog."default" NOT NULL,
    data_de_nascimento date NOT NULL,
    CONSTRAINT usuario_pkey PRIMARY KEY (id)
)