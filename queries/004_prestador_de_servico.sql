--SELECT_MANY
SELECT 
  u.id, 
  u.cpf, 
  u.endereco, 
  u.nome, 
  u.data_de_nascimento, 
  s.informacoes_adicionais 
FROM 
  public."Usuario" AS u 
  LEFT JOIN public."PrestadorDeServico" AS s ON u.id = s.usuario_id
--END-SELECT_MANY

--SELECT
SELECT 
  u.id, 
  u.cpf, 
  u.endereco, 
  u.nome, 
  u.data_de_nascimento, 
  s.informacoes_adicionais 
FROM 
  public."Usuario" AS u 
  LEFT JOIN public."PrestadorDeServico" AS s ON u.id = s.usuario_id 
WHERE 
  u.id = %s
--END-SELECT

--INSERT
INSERT INTO public."PrestadorDeServico" (usuario_id, informacoes_adicionais)
VALUES (%s, %s);
--END-INSERT

--UPDATE
UPDATE public."PrestadorDeServico"
SET 
    usuario_id = %s,
    informacoes_adicionais = %s
WHERE usuario_id = %s;
--END-UPDATE

--DELETE
DELETE FROM public."PrestadorDeServico"
WHERE usuario_id = %s;
--END-DELETE
