-- Table: public.Servico

-- DROP TABLE IF EXISTS public."Servico";

CREATE TABLE IF NOT EXISTS public."Servico"
(
    id integer NOT NULL DEFAULT nextval('"Servico_id_seq"'::regclass),
    nome text COLLATE pg_catalog."default" NOT NULL,
    categoria text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Servico_pkey" PRIMARY KEY (id)
)