CREATE TABLE public."USER"
(
    id integer NOT NULL,
    nome character[] NOT NULL,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public."USER"
    OWNER to "user";