from banco.transacao.Transacao import Transacao
import datetime 

class Historico:
    def __init__(self):
        self.transacoes = []
        self.data_hora = datetime.datetime.now()

    def add_transacao(self, transacao):   
        transacao_dict = {
            "Valor R$": transacao.valor,
            "Tipo de Transação" : transacao.tipo,
            "Data" : self.data_hora.strftime("%d/%m/%Y"),
            "Hora" : self.data_hora.strftime("%H:%M:%S")
        }
        self.transacoes.append(transacao_dict) 

    def get_transacoes(self):
        return self.transacoes  

    def __str__(self):
        return f"{self.transacoes}"        