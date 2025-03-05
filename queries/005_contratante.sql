--SELECT_MANY
SELECT * FROM public."Contratante";
--END-SELECT_MANY

--SELECT
SELECT * FROM public."Contratante"
WHERE usuario_id = %s;
--END-SELECT

--INSERT
INSERT INTO public."Contratante" (usuario_id)
VALUES (%s);
--END-INSERT

--UPDATE
UPDATE public."Contratante"
SET
    usuario_id = %s
WHERE usuario_id = %s;
--END-UPDATE

-- DELETE
DELETE FROM public."Contratante"
WHERE usuario_id = %s;
--END-DELETE