class Cliente:

    def __init__(
        self,
        nome,
        email,
        telefone="",
        codigo_postal="",
        id_cliente=None,
        status=1
    ):
        self.id_cliente = id_cliente
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.codigo_postal = codigo_postal
        self.status = status