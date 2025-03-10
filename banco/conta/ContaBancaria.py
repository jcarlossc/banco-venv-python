from abc import ABC, abstractmethod
from banco.historico.Historico import Historico

class ContaBancaria(ABC):
    def __init__(self, usuario):
        self.usuario = usuario
        self.saldo = 0.0
        self.historico = Historico()

    def get_usuario(self):
        return self.usuario    

    def get_saldo(self):
        return self.saldo

    def get_historico(self):
        return self.historico    

    @abstractmethod
    def get_tipo_conta(self):
        pass    

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass   

    def __str__(self):
        return f"{self.usuario} {self.saldo}"  