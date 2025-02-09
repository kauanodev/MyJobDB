CREATE TABLE public."PrestadorDeServico"
(
    user_id integer NOT NULL references public."Usuario"(id),
    additional_info text,
    PRIMARY KEY (user_id)
);

