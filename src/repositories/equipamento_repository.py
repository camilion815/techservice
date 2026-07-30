from src.database.conexao import conectar
from src.models import equipamento

def inserir(equipamento):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO equipamento (nome, tipo, descricao)
        VALUES (%s, %s, %s)
    """
    valores = (equipamento.nome, equipamento.tipo, equipamento.descricao)

    cursor.execute(sql, valores)
    conexao.commit()
    equipamento.id_equipamento = cursor.lastrowid

    cursor.close()
    conexao.close()
    return equipamento


def listar_equipamentos():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT id_equipamento, nome, tipo, descricao
        FROM equipamento
        WHERE id_equipamento IS NOT NULL
        ORDER BY id_equipamento
    """

    cursor.execute(sql)
    equipamento = cursor.fetchall()

    cursor.close()
    conexao.close()
    return equipamento

def buscar_por_nome(nome):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT id_equipamento, nome, tipo, descricao
        FROM equipamento
        WHERE nome LIKE %s AND id_equipamento IS NOT NULL
        ORDER BY id_equipamento
    """
    valores = (f"%{nome}%",)

    cursor.execute(sql, valores)
    equipamento = cursor.fetchall()

    cursor.close()
    conexao.close()
    return equipamento

def buscar_por_tipo(tipo):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT id_equipamento, nome, tipo, descricao
        FROM equipamento
        WHERE tipo = %s AND id_equipamento IS NOT NULL
        ORDER BY id_equipamento
    """
    valores = (tipo,)

    cursor.execute(sql, valores)
    equipamento = cursor.fetchall()

    cursor.close()
    conexao.close()
    return equipamento



def atualizar(equipamento):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        UPDATE equipamento
        SET nome = %s,
            tipo = %s,
            descricao = %s,
            updated_at = NOW()
        WHERE id_equipamento = %s
          AND status = 1
    """
    valores = (equipamento.nome, equipamento.tipo, equipamento.descricao, equipamento.id_equipamento)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()

def excluir(id_equipamento):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        UPDATE equipamento
        SET status = 0,
            deleted_at = NOW()
        WHERE id_equipamento = %s
          AND status = 1
    """

    cursor.execute(sql, (id_equipamento,))
    conexao.commit()

    cursor.close()
    conexao.close()
