-- Table: public.Servico

-- DROP TABLE IF EXISTS public."Servico";

CREATE SEQUENCE IF NOT EXISTS servico_id_seq;

CREATE TABLE IF NOT EXISTS public."Servico"
(
    id integer NOT NULL DEFAULT nextval('"servico_id_seq"'::regclass),
    nome text COLLATE pg_catalog."default" NOT NULL,
    categoria text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Servico_pkey" PRIMARY KEY (id)
);

ALTER SEQUENCE servico_id_seq
OWNED BY public."Servico".id;
