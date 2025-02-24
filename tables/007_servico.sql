-- Table: public.Servico

-- DROP TABLE IF EXISTS public."Servico";

CREATE TABLE IF NOT EXISTS public."Servico"
(
    id_servico integer NOT NULL,
    nome_servico "char"[] NOT NULL,
    tipo_categoria "char"[] NOT NULL,
    CONSTRAINT "Servico_pkey" PRIMARY KEY (id_servico)
)