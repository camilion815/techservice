class Equipamento:

    def __init__(
        self,
        nome,
        tipo,
        descricao="",
        id_equipamento=None
        

    ):
        self.id_equipamento = id_equipamento
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao
        