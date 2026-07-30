from src.database.conexao import conectar

def inserir(cliente):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO clientes (nome, email, telefone, codigo_postal)
        VALUES (%s, %s, %s, %s)
    """
    valores = (cliente.nome, cliente.email, cliente.telefone, cliente.codigo_postal)

    cursor.execute(sql, valores)
    conexao.commit()
    cliente.id_cliente = cursor.lastrowid

    cursor.close()
    conexao.close()
    return cliente

def listar():
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

def buscar_por_nome(nome):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT id_cliente, nome, email, telefone, codigo_postal, status,
               created_at, updated_at, deleted_at
        FROM clientes
        WHERE nome LIKE %s AND status = 1
        ORDER BY id_cliente
    """
    valores = (f"%{nome}%",)

    cursor.execute(sql, valores)
    clientes = cursor.fetchall()

    cursor.close()
    conexao.close()
    return clientes

def buscar_por_email(email):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT id_cliente, nome, email, telefone, codigo_postal, status,
               created_at, updated_at, deleted_at
        FROM clientes
        WHERE email = %s AND status = 1
    """
    valores = (email,)

    cursor.execute(sql, valores)
    cliente = cursor.fetchone()

    cursor.close()
    conexao.close()
    return cliente

def buscar_por_codigo_postal(codigo_postal):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT id_cliente, nome, email, telefone, codigo_postal, status,
               created_at, updated_at, deleted_at
        FROM clientes
        WHERE codigo_postal = %s AND status = 1
    """
    valores = (codigo_postal,)

    cursor.execute(sql, valores)
    cliente = cursor.fetchone()

    cursor.close()
    conexao.close()
    return cliente



def atualizar(cliente):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        UPDATE clientes
        SET nome = %s,
            email = %s,
            telefone = %s,
            codigo_postal = %s,
            updated_at = NOW()
        WHERE id_cliente = %s
          AND status = 1
    """
    valores = (cliente.nome, cliente.email, cliente.telefone, cliente.codigo_postal, cliente.id_cliente)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()

def excluir(id_cliente):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        UPDATE clientes
        SET status = 0,
            deleted_at = NOW()
        WHERE id_cliente = %s
          AND status = 1
    """

    cursor.execute(sql, (id_cliente,))
    conexao.commit()

    cursor.close()
    conexao.close()

