import unittest

from banco.usuario.PessoaFisica import PessoaFisica
from banco.conta.ContaCorrente import ContaCorrente

class TestContaCorrente(unittest.TestCase):
    """Classe de testes para a classe ContaPoupança."""

    def setUp(self):
        """Configuração do objeto ContaPopança."""
        self.pessoa_fisica = PessoaFisica("jose", "32165498787")
        self.conta_corrente = ContaCorrente(self.pessoa_fisica)

    def test_deposito_valido(self):
        """Teste para validar o depósito em ContaPoupança."""
        self.assertEqual(self.conta_corrente.depositar(500.00), 500.00)       

    def test_saque_valido(self):
        """Teste para validar o saque em ContaPoupança."""
        self.assertEqual(self.conta_corrente.sacar(50.00), 50.00)         

    def test_tipo_conta(self):
        """Teste para validar o depósito em ContaPoupança."""
        self.assertEqual(self.conta_corrente.get_tipo_conta(), "Conta Corrente")   