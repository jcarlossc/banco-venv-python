from banco.conta.ContaBancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def __init__(self, usuario):
        super().__init__(usuario)

    def depositar(self, valor):
        self.saldo += valor  

    def sacar(self, valor):
        self.saldo -= valor 

    def get_tipo_conta(self):
        return "Conta Poupança"       

    def __str__(self):
        return f"{self.usuario} {self.saldo}"   