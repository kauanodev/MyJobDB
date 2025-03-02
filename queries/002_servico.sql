--SELECT_MANY
SELECT * FROM public."Servico";
--END-SELECT_MANY

--SELECT
SELECT * FROM public."Servico" 
WHERE id = %s;
--END-SELECT

--INSERT
INSERT INTO public."Servico" (nome, categoria) 
VALUES (%s, %s);
--END-INSERT

--UPDATE
UPDATE public."Servico"
SET 
    nome = %s,
    categoria = %s
WHERE id = %s;
--END-UPDATE

--DELETE
DELETE FROM public."Servico"
WHERE id = %s;
--END DELETE