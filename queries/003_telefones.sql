--SELECT_MANY
SELECT * FROM public."Telefones";
--END_SELECT_MANY

--SELECT
SELECT * FROM public."Telefones"
WHERE usuario_id = %s;
--END-SELECT

--INSERT
INSERT INTO public."Telefones" (ddd, numero, usuario_id)
VALUES (%s, %s, %s);
--END-INSERT

--UPDATE
UPDATE public."Telefones"
SET                  
    ddd = %s,
    numero = %s
    
WHERE usuario_id = %s;
--END-UPDATE

--DELETE
DELETE FROM public."Telefones"
WHERE usuario_id = %s;
--END-DELETE