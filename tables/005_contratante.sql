-- Table: public.contratante

-- DROP TABLE IF EXISTS public.contratante;

CREATE TABLE IF NOT EXISTS public.contratante
(
    usuario_id integer NOT NULL,
    CONSTRAINT contratante_pkey PRIMARY KEY (usuario_id)
)