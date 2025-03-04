--SELECT_MANY
SELECT 
  * 
FROM 
  public."Solicitacao";
--END-SELECT_MANY

--SELECT
SELECT 
  * 
FROM 
  public."Solicitacao" 
WHERE 
  id = %s;
--END-SELECT

--INSERT
INSERT INTO public."Solicitacao" (
  preco, prazo, descricao, servico_id, 
  contratante_id, prestador_id
) 
VALUES 
  (
    %s, %s, %s, 
    %s, %s, %s
  );
--END-INSERT

--UPDATE
UPDATE 
  public."Solicitacao" 
SET 
  preco = %s, 
  prazo = %s, 
  descricao = %s, 
  servico_id = %s, 
  contratante_id = %s, 
  prestador_id = %s 
WHERE 
  id = %s;
--END-UPDATE

--DELETE
DELETE FROM 
  public."Solicitacao" 
WHERE 
  id = %s;
--END-DELETE
