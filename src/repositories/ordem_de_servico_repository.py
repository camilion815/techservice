from src.database.conexao import conectar
from src.models import ordem_de_servico

def listar(ordem_de_servico):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT
            id_ordem,
            id_cliente,
            id_equipamento,
            diagnostico,
            solucao,
            status,
            prioridade,
            custo_total,
            created_at,
            updated_at
        FROM ordem_de_servico
        ORDER BY id_ordem;
    """

    cursor.execute(sql)
    ordens = cursor.fetchall()

    cursor.close()
    conexao.close()
    return ordens

def criar(ordem_de_servico):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO ordem_de_servico (id_cliente, id_equipamento, diagnostico, solucao, status, prioridade, custo_total)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    valores = (
        ordem_de_servico.id_cliente,
        ordem_de_servico.id_equipamento,
        ordem_de_servico.diagnostico,
        ordem_de_servico.solucao,
        ordem_de_servico.status,
        ordem_de_servico.prioridade,
        ordem_de_servico.custo_total
    )

    cursor.execute(sql, valores)
    conexao.commit()
    ordem_de_servico.id_ordem = cursor.lastrowid

    cursor.close()
    conexao.close()
    return ordem_de_servico

def atualizar(ordem_de_servico):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        UPDATE ordem_de_servico
        SET id_cliente = %s,
            id_equipamento = %s,
            diagnostico = %s,
            solucao = %s,
            status = %s,
            prioridade = %s,
            custo_total = %s,
            updated_at = NOW()
        WHERE id_ordem = %s
    """
    valores = (
        ordem_de_servico.id_cliente,
        ordem_de_servico.id_equipamento,
        ordem_de_servico.diagnostico,
        ordem_de_servico.solucao,
        ordem_de_servico.status,
        ordem_de_servico.prioridade,
        ordem_de_servico.custo_total,
        ordem_de_servico.id_ordem
    )

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()
    
def deletar(ordem_de_servico):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        DELETE FROM ordem_de_servico
        WHERE id_ordem = %s
    """
    valores = (ordem_de_servico.id_ordem,)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()