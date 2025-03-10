from banco.conta.ContaBancaria import ContaBancaria
from banco.transacao.Saque import Saque
from banco.transacao.Deposito import Deposito

class ContaCorrente(ContaBancaria):
    def __init__(self, usuario):
        super().__init__(usuario)

    def depositar(self, valor):
        self.saldo += valor  
        self.historico.add_transacao(Deposito(valor, "Depósito"))

    def sacar(self, valor):
        self.saldo -= valor 
        self.historico.add_transacao(Saque(valor, "Saque"))   

    def get_tipo_conta(self):
        return "Conta Corrente"       

    def __str__(self):
        return f"{self.usuario} {self.saldo}"    