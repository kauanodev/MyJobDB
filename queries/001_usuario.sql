--SELECT_MANY
SELECT * FROM public."Usuario";
--END-SELECT_MANY

--SELECT
SELECT * FROM public."Usuario"
WHERE id = %s;
--END-SELECT

--INSERT
INSERT INTO public."Usuario" (id, cpf, endereco, nome, data_de_nascimento)
VALUES (%s, %s, %s, %s, %s);
--END-INSERT

-- UPDATE
UPDATE public."Usuario"
SET
    cpf = %s,
    endereco = %s,
    nome = %s,
    data_de_nascimento = %s
WHERE id = %s;
--END-UPDATE

-- DELETE
DELETE FROM public."Usuario"
WHERE id = %s;
--END-DELETE