from src.database.conexao import conectar
from src.models import ordem_de_servico

def listar_ordens():
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