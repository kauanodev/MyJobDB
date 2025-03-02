-- Table: public.Contratante

-- DROP TABLE IF EXISTS public."Contratante";

CREATE TABLE IF NOT EXISTS public."Contratante"
(
    usuario_id integer NOT NULL,
    CONSTRAINT contratante_pkey PRIMARY KEY (usuario_id)
);
