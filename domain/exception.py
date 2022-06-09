class FillStockError(Exception):
    def __init__(self):
        default_message = 'Preencha ao menos 4 letras do ativo'
        super().__init__(default_message)


class NameStockError(Exception):
    def __init__(self):
        default_message = 'Ativo não encontrado'
        super().__init__(default_message)
