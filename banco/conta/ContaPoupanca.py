from banco.conta.ContaBancaria import ContaBancaria
from banco.transacao.Deposito import Deposito
from banco.transacao.Saque import Saque

class ContaPoupanca(ContaBancaria):
    def __init__(self, usuario):
        super().__init__(usuario)

    def depositar(self, valor):
        self.saldo += valor  
        self.historico.add_transacao(Deposito(valor, "Depósito"))
        return valor

    def sacar(self, valor):
        self.saldo -= valor 
        self.historico.add_transacao(Saque(valor, "Saque"))   
        return valor

    def get_tipo_conta(self):
        return "Conta Poupança"       

    def __str__(self):
        return f"{self.usuario} {self.saldo}"   