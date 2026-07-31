from src.database.conexao import conectar
from src.models import equipamento

def listar(equipamento):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT
            id_equipamento,
            id_cliente,
            tipo,
            marca,
            modelo,
            numero_serie,
            status,
            created_at,
            updated_at
        FROM equipamento
        ORDER BY id_equipamento;
    """

    cursor.execute(sql)
    equipamento = cursor.fetchall()

    cursor.close()
    conexao.close()
    return equipamento

def criar(equipamento):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO equipamento (id_equipamento, tipo, marca, modelo, numero_serie, status)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    valores = (
        equipamento.id_equipamento,
        equipamento.tipo,
        equipamento.marca,
        equipamento.modelo,
        equipamento.numero_serie,
        equipamento.status
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
        SET id_equipamento = %s,
            tipo = %s,
            marca = %s,
            modelo = %s,
            numero_serie = %s,
            status = %s,
            updated_at = NOW()
        WHERE id_equipamento = %s
    """
    valores = (
        equipamento.id_equipamento,
        equipamento.tipo,
        equipamento.marca,
        equipamento.modelo,
        equipamento.numero_serie,
        equipamento.status,
        equipamento.id_equipamento
    )

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()
    return equipamento

def deletar(id_equipamento):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "DELETE FROM equipamento WHERE id_equipamento = %s"
    cursor.execute(sql, (id_equipamento,))
    conexao.commit()

    cursor.close()
    conexao.close()
