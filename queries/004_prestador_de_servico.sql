SELECT * FROM public."Usuario" AS u 
LEFT JOIN public."PrestadorDeServico" AS s ON u.id = s.usuario_id
WHERE u.id = %s

INSERT INTO public."PrestadorDeServico" (usuario_id, informacoes_adicionais)
VALUES (%s, %s);

UPDATE public."PrestadorDeServico"
SET 
    usuario_id = %s,
    informacoes_adicionais = %s
WHERE usuario_id = %s;

DELETE FROM public."PrestadorDeServico"
WHERE usuario_id = %s;
