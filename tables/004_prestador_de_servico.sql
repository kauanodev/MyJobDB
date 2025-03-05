CREATE TABLE IF NOT EXISTS public."PrestadorDeServico"
(
    usuario_id INTEGER NOT NULL references public."Usuario"(id),
    informacoes_adicionais TEXT,
    PRIMARY KEY (usuario_id)
);

