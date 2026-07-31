from src.database.conexao import conectar

def listar(cliente):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT
            id_cliente,
            nome,
            email,
            telefone,
            endereco,
            created_at,
            updated_at
        FROM clientes
        ORDER BY id_cliente;
    """

    cursor.execute(sql)
    clientes = cursor.fetchall()

    cursor.close()
    conexao.close()
    return clientes

def criar(cliente):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO clientes (nome, email, telefone, endereco)
        VALUES (%s, %s, %s, %s)
    """
    valores = (
        cliente.nome,
        cliente.email,
        cliente.telefone,
        cliente.endereco
    )

    cursor.execute(sql, valores)
    conexao.commit()
    cliente.id_cliente = cursor.lastrowid

    cursor.close()
    conexao.close()
    return cliente

def atualizar(cliente):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        UPDATE clientes
        SET nome = %s, email = %s, telefone = %s, endereco = %s
        WHERE id_cliente = %s
    """
    valores = (
        cliente.nome,
        cliente.email,
        cliente.telefone,
        cliente.endereco,
        cliente.id_cliente
    )

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()
    return cliente

def deletar(cliente):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "DELETE FROM clientes WHERE id_cliente = %s"
    valores = (cliente.id_cliente,)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()
