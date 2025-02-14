-- Table: public.usuario

-- DROP TABLE IF EXISTS public.usuario;

CREATE TABLE IF NOT EXISTS public.usuario
(
    id integer NOT NULL,
    cpf character varying(11) COLLATE pg_catalog."default" NOT NULL,
    endereco text COLLATE pg_catalog."default" NOT NULL,
    nome character varying(255) COLLATE pg_catalog."default" NOT NULL,
    "data_de_nascimento de " date NOT NULL,
    CONSTRAINT usuario_pkey PRIMARY KEY (id)
)