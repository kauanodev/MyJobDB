from app.db.connection import db_connection
from psycopg2.extensions import cursor as Cursor


def create_seeds():
    connection = db_connection()
    cursor: Cursor = connection.cursor()
    cursor.execute('SELECT COUNT(*) FROM public."Usuario";')
    if cursor.fetchone()[0] == 0:
        seed_data_usuario = """
            INSERT INTO public."Usuario" (cpf, endereco, nome, data_de_nascimento) VALUES
            ('12345678901', 'Rua A, 123, São Paulo, SP', 'João Silva', '1990-05-14'),
            ('23456789012', 'Avenida B, 456, Rio de Janeiro, RJ',
             'Maria Oliveira', '1985-10-22'),
            ('34567890123', 'Rua C, 789, Salvador, BA',
             'Carlos Santos', '1992-03-09'),
            ('45678901234', 'Praça D, 101, Brasília, DF', 'Ana Costa', '1988-04-01'),
            ('56789012345', 'Rua E, 202, Fortaleza, CE',
             'Lucas Pereira', '1995-08-30');
            """
        print(seed_data_usuario)
        cursor.execute(seed_data_usuario)

    cursor.execute('SELECT COUNT(*) FROM public."Servico";')
    if cursor.fetchone()[0] == 0:
        seed_data_servico = """
        INSERT INTO public."Servico" (nome, categoria) VALUES
        ('Limpeza', 'Serviços Domésticos'),
        ('Encanamento', 'Serviços Técnicos'),
        ('Pintura', 'Serviços de Construção'),
        ('Jardinagem', 'Serviços de Jardinagem'),
        ('Aulas Particulares', 'Educação');
        """
        print(seed_data_servico)
        cursor.execute(seed_data_servico)

    cursor.execute('SELECT COUNT(*) FROM public."PrestadorDeServico";')
    if cursor.fetchone()[0] == 0:
        seed_data_prestador = """
        INSERT INTO public."PrestadorDeServico" (user_id, additional_info) VALUES
        (1, 'Profissional com 5 anos de experiência em limpeza.'),
        (2, 'Encanador experiente, atende toda a região.'),
        (3, 'Pintor profissional, especializado em casas e apartamentos.'),
        (4, 'Jardineiro, cuida de jardins e paisagismo.'),
        (5, 'Aulas de matemática e física para alunos do ensino médio.');
        """
        print(seed_data_prestador)
        cursor.execute(seed_data_prestador)

    cursor.execute('SELECT COUNT(*) FROM public."Contratante";')
    if cursor.fetchone()[0] == 0:
        seed_data_contratante = """
        INSERT INTO public."Contratante" (usuario_id) VALUES
        (1),
        (2),
        (3);
        """
        print(seed_data_contratante)
        cursor.execute(seed_data_contratante)

    connection.commit()
