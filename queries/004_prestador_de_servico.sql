--SELECT_MANY
SELECT * FROM public."Usuario" AS u
LEFT JOIN public."PrestadorDeServico" AS s ON u.id = s.user_id
--END-SELECT_MANY

--SELECT
SELECT * FROM public."Usuario" AS u 
LEFT JOIN public."PrestadorDeServico" AS s ON u.id = s.user_id
WHERE u.id = %s
--END-SELECT

--INSERT
INSERT INTO public."PrestadorDeServico" (user_id, additional_info)
VALUES (%s, %s);
--END-INSERT

--UPDATE
UPDATE public."PrestadorDeServico"
SET 
    additional_info = %s
WHERE user_id = %s;
--END-UPDATE

--DELETE
DELETE FROM public."PrestadorDeServico"
WHERE user_id = %s;
--END-DELETE
