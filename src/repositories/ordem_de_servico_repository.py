from src.database.conexao import conectar
from src.models import ordem_de_servico

def inserir(ordem):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO ordem_de_servico (cliente_id, equipamento_id, diagnostico, solucao, status, prioridade, custo_total)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    valores = (ordem.cliente_id, ordem.equipamento_id, ordem.diagnostico, ordem.solucao,
               ordem.status, ordem.prioridade, ordem.custo_total)

    cursor.execute(sql, valores)
    conexao.commit()
    ordem.id = cursor.lastrowid

    cursor.close()
    conexao.close()
    return ordem

