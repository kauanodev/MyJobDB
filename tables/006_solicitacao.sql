-- Table: public.Solicitacao

-- DROP TABLE IF EXISTS public."Solicitacao";

CREATE TABLE IF NOT EXISTS public."Solicitacao" (
  id SERIAL NOT NULL PRIMARY KEY, 
  preco DECIMAL(10, 2) NOT NULL, 
  prazo TIMESTAMP NOT NULL, 
  descricao TEXT, 
  servico_id INTEGER NOT NULL REFERENCES public."Servico"(id), 
  contratante_id INTEGER NOT NULL REFERENCES public."Contratante"(usuario_id), 
  prestador_id INTEGER REFERENCES public."PrestadorDeServico"(usuario_id)
);

