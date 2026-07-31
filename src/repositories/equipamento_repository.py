from src.database.conexao import conectar


def listar(equipamento):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT
            id_equipamento,
            nome,
            tipo,
            descricao,
            created_at,
            updated_at
        FROM equipamento
        ORDER BY id_equipamento;
    """

    cursor.execute(sql)
    equipamentos = cursor.fetchall()

    cursor.close()
    conexao.close()
    return equipamentos


def criar(equipamento):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO equipamento (nome, tipo, descricao)
        VALUES (%s, %s, %s)
    """

    valores = (
        equipamento.nome,
        equipamento.tipo,
        equipamento.descricao
    )

    cursor.execute(sql, valores)
    conexao.commit()
    equipamento.id_equipamento = cursor.lastrowid

    cursor.close()
    conexao.close()

    return equipamento


def atualizar(equipamento):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        UPDATE equipamento
        SET
            nome = %s,
            tipo = %s,
            descricao = %s
        WHERE id_equipamento = %s
    """

    valores = (
        equipamento.nome,
        equipamento.tipo,
        equipamento.descricao,
        equipamento.id_equipamento
    )

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()

    return equipamento


def deletar(equipamento):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "DELETE FROM equipamento WHERE id_equipamento = %s"
    valores = (equipamento.id_equipamento,)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()