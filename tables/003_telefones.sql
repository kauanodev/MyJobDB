CREATE TABLE IF NOT EXISTS public."Telefones" (
 ddd int NOT NULL,
 numero text NOT NULL,
 usuario_id int NOT NULL,
 PRIMARY KEY ("ddd","numero","usuario_id"),
 FOREIGN KEY (usuario_id) REFERENCES public."Usuario" (id)
);
