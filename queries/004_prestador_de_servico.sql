SELECT * FROM public."Usuario" AS u 
LEFT JOIN public."PrestadorDeServico" AS s ON u.id = s.user_id
WHERE u.id = %s

INSERT INTO public."PrestadorDeServico" (user_id, additional_info)
VALUES (%s, %s);

UPDATE public."PrestadorDeServico"
SET 
    user_id = %s,
    additional_info = %s
WHERE user_id = %s;

DELETE FROM public."PrestadorDeServico"
WHERE user_id = %s;
