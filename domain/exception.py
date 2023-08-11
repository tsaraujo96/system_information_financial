class NotHaveDataError(Exception):
    def __init__(self):
        default_message = "Período ou Ativo sem dados"
        super().__init__(default_message)


class NameStockError(Exception):
    def __init__(self):
        default_message = "Ativo não encontrado"
        super().__init__(default_message)
