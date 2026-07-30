
class ordem_de_servico:
    def __init__(self, id, cliente_id, equipamento_id, diagnostico, solucao, status, prioridade, custo_total):
        self.id = id
        self.cliente_id = cliente_id
        self.equipamento_id = equipamento_id
        self.diagnostico = diagnostico
        self.solucao = solucao
        self.status = status
        self.prioridade = prioridade
        self.custo_total = custo_total