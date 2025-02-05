-- Table: public.contratante

-- DROP TABLE IF EXISTS public.contratante;

CREATE TABLE IF NOT EXISTS public.contratante
(
    avaliacao numeric NOT NULL
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.contratante
    OWNER to postgres;