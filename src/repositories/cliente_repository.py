from src.database.conexao import conectar

def listar_clientes():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT id_cliente, nome, email, telefone, codigo_postal, status,
               created_at, updated_at, deleted_at
        FROM clientes
        WHERE status = 1
        ORDER BY id_cliente
    """

    cursor.execute(sql)
    clientes = cursor.fetchall()

    cursor.close()
    conexao.close()
    return clientes
