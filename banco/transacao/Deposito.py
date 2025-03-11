from banco.transacao.Transacao import Transacao

class Deposito(Transacao):
    def __init__(self, valor, tipo):
        super().__init__(valor, tipo)

    def get_valor(self):
        return self.valor  
    
    def get_tipo(self):
        return self.tipo

    def __str__(self):
        return f"{self.valor} {self.tipo}"     